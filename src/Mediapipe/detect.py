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
  output_path = filepath
  output_name = str(time.time())+gl.get_state()
  stored_landmarks = []
  stored_angles = []
  
  match (gl.get_state()):
    case "mp_live": 			
      cap = cv2.VideoCapture(0)	
      while cap.isOpened() and gl.get_state() == "mp_live":
        process(cap, stored_landmarks, stored_angles)
      cap.release()		
      
    case "mp_file":
      if (not filename): return 
      cap = cv2.VideoCapture(filename)
      while cap.isOpened() and gl.get_state() == "mp_file":
        process(cap, stored_landmarks, stored_angles)
      cap.release()

  
  writer.write_csv_to_xlsx([
                              ('landmarks', writer.get_landmarks_csv(stored_landmarks)),
                              ('angles', writer.get_angles_csv(stored_angles))
                          ], 
                          output_path, output_name)
          
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
    # mh.show_angles(angles)