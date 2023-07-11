import os
from tkinter import filedialog
import Mediapipe.detect as mpd
import Program.globalv as gl
import pathlib

path = pathlib.Path().resolve()
video_formats = [".mp4", ".mov", "avi", ".wmv", ".webm"]
image_formats = [".png", ".jpg"]

def start_mediapipe_live_video()->None:
  gl.set_state("mp_live")
  mpd.detect()

def start_mediapipe_from_file()->None:
  file = filedialog.askopenfilename(initialdir=path, title = "Select a file", filetypes=[("Video or image file", video_formats+image_formats)])
  if not file: return
  gl.set_state("mp_file")
  mpd.detect(file)

def save_file(default_path:str, default_name:str, default_type: str, default_extensions: list[str])->None:
  return filedialog.asksaveasfilename(initialdir= default_path,initialfile = default_name, defaultextension=default_extensions[0], filetypes=[(default_type, default_extensions)])
  