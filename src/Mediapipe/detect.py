from pathlib import Path
import time
import cv2
import mediapipe as mp
import Mediapipe.mediapipe_helper as mh
import Program.globalv as gl
import Writer.writer as writer
import pathlib

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=gl.get_min_tracking_confidence(), 
                    min_detection_confidence=gl.get_min_detection_confidence())
path = pathlib.Path().resolve()


def detect(filename: str=None): 
	filepath = str(path) + "\\output\\"	
	Path(filepath).mkdir(parents=True, exist_ok=True)
	output_path = filepath+str(time.time())+gl.get_state()
	output_angles = output_path+"_angles"
	output_landmarks = output_path+"_landmarks"
	stored_landmarks = []
	stored_angles = []
	
	match (gl.get_state()):
		case "mp_live": 			
			cap = cv2.VideoCapture(0)	
			output_path = filepath+str(time.time())+"_live"
			while cap.isOpened() and gl.get_state() == "mp_live":
				process(cap, stored_landmarks, stored_angles)
			cap.release()		
			
		case "mp_image":
			if (not filename): return
			cap = cv2.VideoCapture(filename)
			output_path = filepath+str(time.time())+"_image"
			process(cap, stored_landmarks, stored_angles)
			cap.release()			
		
		case "mp_video":
			if (not filename): return 
			cap = cv2.VideoCapture(filename)
			output_path = filepath+str(time.time())+"_video"
			while cap.isOpened() and gl.get_state() == "mp_video":
				process(cap, stored_landmarks, stored_angles)
			cap.release()
			writer.print_landmarks_data_csv(stored_landmarks, output_landmarks)
			writer.print_angles_data_csv(stored_angles, output_angles)
					
def process(cap, stored_landmarks:list=[], stored_angles:list=[]):
	image, results = mh.read_frame(cap, pose, mp_drawing, mp_pose)		
	if image is None: 
		cap.release()	
		return 
	mh.show_frame(image)
	landmarks = results.pose_landmarks
	if (landmarks is not None):
		stored_landmarks.append(landmarks.landmark)
		angles = mh.get_angles(landmarks.landmark)
		stored_angles.append(angles)
		#writer.print_angles(angles, output_angles)
		#writer.print_landmarks(landmarks.landmark, output_landmarks)
		mh.show_angles(angles)