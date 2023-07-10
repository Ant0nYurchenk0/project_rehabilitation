import os

landmark_names = ['nose', 'left_eye_inner', 'left_eye', 'left_eye_outer',
                    'right_eye_inner', 'right_eye', 'right_eye_outer', 'left_ear', 
                    'right_ear', 'mouth_left', 'mouth_right', 'left_shoulder', 'right_shoulder', 
                    'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky', 
                    'left_index','right_index', 'left_thumb', 'right_thumb', 'left_hip', 'right_hip', 
                    'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_heel', 'right_heel',
                    'left_foot_index', 'right_foot_index']

def print_landmarks(landmarks: list[str], filename: str)->None:
  if (filename is not None):
    file_with_extension = filename+".csv"
  else:
    return
  output_file = open(file_with_extension, "a+")
  if os.stat(file_with_extension).st_size == 0:
    for i in range(len(landmark_names)):
      output_file.write(','+ str(landmark_names[i])+','*3)  
  for i in range(len(landmarks)):
      output_file.write(','+ str(landmarks[i].x)+','+str(landmarks[i].y)+','+str(landmarks[i].z)+',')
  output_file.write('\n')

def print_angles(angles: dict[str, float], filename: str=None)->None:    
  if (filename is not None):
    output_file = open(filename+".csv", "a+")
    write_func = output_file.write
  else:
     write_func = lambda content: print(content, end='')
  for angle in angles: 
    write_func(str(angle) + "," + str(angles[angle])+'\n')
  write_func("\n")


def print_landmarks_data_csv(landmarks_data: list[list[str]], filename: str="landmarks_output")->None:
  if (filename is not None):
    file_with_extension = filename+".csv"
  else:
    return
  output_file = open(file_with_extension, "a+")
  if os.stat(file_with_extension).st_size == 0:
    for i in range(len(landmark_names)):
      output_file.write(','+ str(landmark_names[i])+','*3)
  for landmarks in landmarks_data:
    output_file.write("\n")
    for i in range(len(landmarks)):
        output_file.write(','+ str(landmarks[i].x)+','+str(landmarks[i].y)+','+str(landmarks[i].z)+',')
  output_file.close()

def print_angles_data_csv(angles_data: list[dict[str, float]], filename: str="angles_output")->None:    
  if (filename is not None):
    output_file = open(filename+".csv", "a+")
    write_func = output_file.write
  else:
     write_func = lambda content: print(content, end='')
  for angles in angles_data:
    for angle in angles: 
      write_func(str(angle) + "," + str(angles[angle])+'\n')
    write_func("\n")
  output_file.close()


def clear_file(filename: str)->None:
  open(filename, "w+")