from pathlib import Path
import time
import cv2
import mediapipe as mp
import Mediapipe.mediapipe_helper as mh
import Program.globalv as gl
import Writer.writer as writer
import pathlib
from datetime import timedelta


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=gl.get_min_tracking_confidence(), 
                    min_detection_confidence=gl.get_min_detection_confidence())
path = pathlib.Path().resolve()

frame_count = 0
total_frames = 0
frames = []

def detect(filename: str=None): 
  filepath = str(path) + "\\output\\"	
  Path(filepath).mkdir(parents=True, exist_ok=True)
  output_path = filepath
  output_name = str(time.time())+gl.get_state()
  stored_landmarks = []
  stored_timestamps = []
  stored_angles = []

  global frame_count
  global total_frames

  total_frames = 0
  frame_count=0
  
  match (gl.get_state()):
    case "mp_live": 			
      cap = cv2.VideoCapture(0)	
      while cap.isOpened() and gl.get_state() == "mp_live":
        process(cap, stored_landmarks, stored_angles)
      cap.release()		
      
    case "mp_file":
      if (not filename): return 
      cap = cv2.VideoCapture(filename)
      gl.total_duration = mh.get_video_duration(cap)
      total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
      while cap.isOpened() and gl.get_state() == "mp_file":
        process(cap, stored_landmarks, stored_angles, stored_timestamps)
      cap.release()
  
  writer.write_csv_to_xlsx([
        ('timestamps', writer.get_timestamps_csv(stored_timestamps)),
        ('landmarks', writer.get_landmarks_csv(stored_landmarks)),
        ('angles', writer.get_angles_csv(stored_angles))
    ], output_path, output_name)
  
  global frames
  writer.output_video(frames, output_path, output_name)
  frames.clear()

          
def process(cap, stored_landmarks: list = [], stored_angles: list = [], stored_timestamps: list = []):
    if gl.start_time is None:
        gl.start_time = time.time()
    
    image, results = mh.read_frame(cap, pose, mp_drawing, mp_pose)
    if image is None: 
        cap.release()	
        return 
    image = cv2.flip(image,1)
    
    # Get the current timestamp
    timestamp = time.time()
    global frame_count
    global total_frames
    frame_count += 1

    # Calculate the elapsed time as a fraction of total duration based on frame count
    if gl.total_duration and frame_count > 1:
        elapsed_time = gl.total_duration * frame_count / total_frames
        gl.elapsed_time = elapsed_time

        elapsed_time = timedelta(seconds=elapsed_time)
        elapsed_seconds = elapsed_time.seconds
        elapsed_microseconds = elapsed_time.microseconds

        total_time = timedelta(seconds=gl.total_duration)
        total_seconds = total_time.seconds
        total_microseconds = total_time.microseconds

        timestamp_str = f"{elapsed_seconds}:{str(elapsed_microseconds)[:2]} / {total_seconds}:{str(total_microseconds)[:2]}"

        image = cv2.putText(image, 
                            text = timestamp_str,
                            org = (50, 50), 
                            fontFace = cv2.FONT_HERSHEY_SIMPLEX,  
                            fontScale = 1, 
                            color = (255, 0, 0), 
                            thickness = 2, 
                            lineType = cv2.LINE_AA)
    else:
        gl.elapsed_time = None
  
    

    mh.show_frame(image)
    global frames
    frames.append(image)

    landmarks = results.pose_landmarks
    if landmarks is not None:
        # Add the timestamp to the stored timestamps
        stored_timestamps.append(timestamp)
        # Add the landmarks data
        stored_landmarks.append(landmarks.landmark)
        angles = mh.get_angles(landmarks.landmark)
        stored_angles.append(angles)


