import tkinter as tk 
import Tkinter.tkinter_helper as th
import Tkinter.tkinter_functions as tf
import Program.label_control as lc

def main():
  root = tk.Tk()
  root.title('GymBro - testing')
  root.geometry('x')
  root_menu = tk.Menu(root)
  root.config(menu=root_menu)

  #window menu
  window_menu = th.add_menu(root_menu, "Window")
  th.add_command_to_menu(window_menu, "Exit", root.quit)

  #========creating frames=========
  
  angles_frame = th.add_frame(root, 0,400,"green", 300, 700)

  th.add_label(angles_frame, 0, 10, 'Лівий лікоть')
  lc.add_label("left_elbow",  th.add_label(angles_frame, 121, 10, '0'))

  th.add_label(angles_frame, 0, 51, 'Ліве плече')
  lc.add_label("left_shoulder", th.add_label(angles_frame, 121, 51, '0'))

  th.add_label(angles_frame, 0, 92, 'Ліве коліно')
  lc.add_label("left_knee", th.add_label(angles_frame, 121, 92, '0'))

  th.add_label(angles_frame, 350, 10, 'Правий лікоть')
  lc.add_label("right_elbow", th.add_label(angles_frame, 500, 10, '0'))

  th.add_label(angles_frame, 350, 51, 'Праве плече')
  lc.add_label("right_shoulder", th.add_label(angles_frame, 500, 51, '0'))

  th.add_label(angles_frame, 350, 92, 'Праве коліно')
  lc.add_label("right_knee", th.add_label(angles_frame, 500, 92, '0'))


  mp_live_frame = th.add_frame(root, 0,0,"blue", 400, 700)
  lc.add_label("image",  th.add_label(mp_live_frame, 0, 0, ''))

  #mediapipe menu
  mediapipe_menu = th.add_menu(root_menu, "Mediapipe")
  th.add_command_to_menu(mediapipe_menu, "Live Video", lambda: tf.start_mediapipe_live_video())
  th.add_command_to_menu(mediapipe_menu, "Video file", lambda: tf.start_mediapipe_stored_video())
  th.add_command_to_menu(mediapipe_menu, "Image file", lambda: tf.start_mediapipe_stored_image())

  root.mainloop()


