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
	match (gl.get_state()):
		case "mp_live": 			
			cap = cv2.VideoCapture(0)	
			output_path = str(path) + "\\output\\"+str(time.time())+"_live"
			writer.clear_file(output_path)
			while cap.isOpened() and gl.get_state() == "mp_live":
				process(cap, output_path)
			cap.release()		
			
		case "mp_image":
			if (not filename): return
			cap = cv2.VideoCapture(filename)
			output_path = str(path) + "\\output\\"+str(time.time())+"_image"
			writer.clear_file(output_path)
			process(cap, output_path)
			cap.release()			
		
		case "mp_video":
			if (not filename): return 
			cap = cv2.VideoCapture(filename)
			output_path = str(path) + "\\output\\"+str(time.time())+"_video"
			writer.clear_file(output_path)
			while cap.isOpened() and gl.get_state() == "mp_video":
				process(cap, output_path)
			cap.release()
					
def process(cap, filepath:str=None):
	image, results = mh.read_frame(cap, pose, mp_drawing, mp_pose)		
	if image is None: 
		cap.release()	
		return 
	mh.show_frame(image)
	landmarks = results.pose_landmarks
	if (landmarks is not None):
		angles = mh.get_angles(landmarks.landmark)
		writer.print_angles(angles, filepath+"_angles")	
		writer.print_landmarks(landmarks.landmark, filepath+"_landmarks")			
		mh.show_angles(angles)