
import csv
from io import StringIO
from xlsxwriter.workbook import Workbook
import Tkinter.tkinter_functions as tf
import cv2

landmark_names = ['nose', 'left_eye_inner', 'left_eye', 'left_eye_outer',
                    'right_eye_inner', 'right_eye', 'right_eye_outer', 'left_ear', 
                    'right_ear', 'mouth_left', 'mouth_right', 'left_shoulder', 'right_shoulder', 
                    'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky', 
                    'left_index','right_index', 'left_thumb', 'right_thumb', 'left_hip', 'right_hip', 
                    'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_heel', 'right_heel',
                    'left_foot_index', 'right_foot_index']

def get_landmarks_csv(landmarks_data: list[list[str]])->str:
  result = ""
  for i in range(len(landmark_names)):
    result += ','+ str(landmark_names[i]) + ','*3
  for landmarks in landmarks_data:
    result += "\n"
    for i in range(len(landmarks)):
      result += ','+ str(landmarks[i].x) + ','+str(landmarks[i].y) + ','+str(landmarks[i].z) + ','
  return result

def get_angles_csv(angles_data: list[dict[str, float]])->str:   
  result = ""
  for angle in angles_data[0]:
    result += ','+ str(angle) + ','
  for angles in angles_data:
    result +="\n"
    for angle in angles: 
      result +="," + str(angles[angle]) + ','
  return result

from datetime import datetime
def get_timestamps_csv(timestamps_data: list[float]) -> str:
    result = "Timestamp\n"
    for timestamp in timestamps_data:
        formatted_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
        result += formatted_time + "\n"
    return result


def write_csv_to_xlsx(texts: list[(str, str)], default_path: str, default_name: str) -> None:
    name = tf.save_file(default_path, default_name, "Excel Sheet", ['.xlsx'])
    if name == '': return 

    workbook = Workbook(name)

    for text in texts:
        f = StringIO(text[1])
        reader = csv.reader(f, delimiter=',')
        worksheet = workbook.add_worksheet()
        if text[0] == 'Timestamp':
            # If it's timestamps, write them as the first column
            data = [float(row[0]) for row in reader]
            worksheet.write_column('A1', data)
        else:
            # Otherwise, write data as usual
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    try: 
                      value = float(col)
                      worksheet.write_number(r,c,value)
                    except:
                      worksheet.write(r, c, col)

        worksheet.name = text[0]

    workbook.close()

def output_video(frames: [], default_path: str, default_name: str):
  if len(frames) == 0:
    return
  elif len(frames) == 1:
    file_format = '.jpg'
    file_type = 'Image'
    func = write_image
  elif len(frames) > 1:
    file_format = '.mp4'
    file_type = 'Video'
    func = write_video

  name = tf.save_file(default_path, default_name, file_type, [file_format])

  if name == '': return

  func(name, frames)

def write_image(path, frames):
   cv2.imwrite(path, frames[0]) 

def write_video(path, frames):
  height, width, _ = frames[0].shape
  out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))
  [out.write(f) for f in frames]
  out.release()