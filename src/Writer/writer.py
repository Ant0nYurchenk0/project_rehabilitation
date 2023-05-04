landmark_names = ['nose', 'left_eye_inner', 'left_eye', 'left_eye_outer',
                   'right_eye_inner', 'right_eye', 'right_eye_outer', 'left_ear', 
                   'right_ear', 'mouth_left', 'mouth_right', 'left_shoulder', 'right_shoulder', 
                   'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky', 
                   'left_index','right_index', 'left_thumb', 'right_thumb', 'left_hip', 'right_hip', 
                   'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_heel', 'right_heel',
                     'left_foot_index', 'right_foot_index']

def print_landmarks(landmarks)->None:
  for i in range(len(landmarks)):
      print(landmark_names[i] +' \n x: ' + str(landmarks[i].x)+', \n y: '+str(landmarks[i].y)+', \n z: '+str(landmarks[i].z)+'\n')
  print('-'*10)

def print_angles(angles: dict[str, float], filename: str=None)->None:    
  if (filename is not None):
    output_file = open(filename, "a+")
    write_func = output_file.write
  else:
     write_func = lambda content: print(content, end='')
  for angle in angles: 
    write_func(str(angle) + " = " + str(angles[angle])+'\n')
  write_func('-'*10+"\n")

def clear_file(filename: str)->None:
  open(filename, "w+")