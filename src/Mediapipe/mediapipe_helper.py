import cv2
from PIL import Image, ImageTk 
import Math.calculate_angle as m
import Program.angles as angle
import Program.label_control as lc

def read_frame(cap, pose, mp_drawing, mp_pose):
  _, frame = cap.read()
  if frame is None: return (None, None)
  image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
  results = pose.process(image)
          
  mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
    mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5), 
    mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10))
  
  return (image, results)

def show_frame(image):
  image = cv2.flip(image,1)
  img = image[:, :, :] 
  imgarr = Image.fromarray(img) 
  aspect_ratio = imgarr.width/imgarr.height
  imgarr = imgarr.resize((int(aspect_ratio*400), 400))
  imgtk = ImageTk.PhotoImage(imgarr) 
  lc.set_image("image", imgtk)
  
def get_angles(landmarks)->dict[str, float]:
  angles = {}  
  angles["left_elbow"]=m.calculate_angle(get_angle_points_list(angle.get_left_elbow(), landmarks))
  angles["right_elbow"]=m.calculate_angle(get_angle_points_list(angle.get_right_elbow(), landmarks))
  angles["left_shoulder"]=m.calculate_angle(get_angle_points_list(angle.get_left_shoulder(), landmarks))
  angles["right_shoulder"]=m.calculate_angle(get_angle_points_list(angle.get_right_shoulder(), landmarks))
  angles["left_knee"]=m.calculate_angle(get_angle_points_list(angle.get_left_knee(), landmarks))
  angles["right_knee"]=m.calculate_angle(get_angle_points_list(angle.get_right_knee(), landmarks))
  angles["right_hip"]=m.calculate_angle(get_angle_points_list(angle.get_right_hip(), landmarks))
  angles["left_hip"]=m.calculate_angle(get_angle_points_list(angle.get_left_hip(), landmarks))
  return angles

def show_angles(angles: dict[str, float]):
  for angle in angles:
    lc.set_text(angle, round(angles[angle], 3))

def get_angle_points_list(angle_config: list[int], landmarks)->list[list[float]]:
  a = [landmarks[angle_config[0]].x,landmarks[angle_config[0]].y]
  b = [landmarks[angle_config[1]].x,landmarks[angle_config[1]].y]
  c = [landmarks[angle_config[2]].x,landmarks[angle_config[2]].y]
  return [a, b, c]

def get_video_duration(cap):
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    duration_seconds = total_frames / fps
    return duration_seconds

def update_timers(start_time, elapsed_time, total_duration):
  lc.update_timer_label("timer", start_time, elapsed_time, total_duration)
