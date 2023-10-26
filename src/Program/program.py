import tkinter as tk 
import Tkinter.tkinter_helper as th
import Tkinter.tkinter_functions as tf
import Program.label_control as lc
def main():
  root = tk.Tk()
  root.title('GymBro - testing')
  root.geometry('700x400')
  root_menu = tk.Menu(root)
  root.config(menu=root_menu)

  #window menu
  window_menu = th.add_menu(root_menu, "Window")
  th.add_command_to_menu(window_menu, "Exit", root.quit)

  #========creating frames=========

  mp_live_frame = th.add_frame(root, 0,0,"blue", 400, 700)
  lc.add_label("image",  th.add_label(mp_live_frame, 0, 0, ''))

  #mediapipe menu
  mediapipe_menu = th.add_menu(root_menu, "Mediapipe")
  th.add_command_to_menu(mediapipe_menu, "Live Video", lambda: tf.start_mediapipe_live_video())
  th.add_command_to_menu(mediapipe_menu, "From file", lambda: tf.start_mediapipe_from_file())


  root.mainloop()


