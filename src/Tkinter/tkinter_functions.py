from tkinter import filedialog
import tkinter as tk 
import Mediapipe.detect as mpd
import Program.globalv as gl
import pathlib

path = pathlib.Path().resolve()

def start_mediapipe_live_video()->None:
  gl.set_state("mp_live")
  mpd.detect()

def start_mediapipe_stored_video()->None:
  filename = filedialog.askopenfilename(initialdir=path, title = "Select a file", filetypes=[("Video files", "*.mp4")])
  if (not filename): return
  gl.set_state("mp_video")
  mpd.detect(filename)

def start_mediapipe_stored_image()->None:
  filename = filedialog.askopenfilename(initialdir=path, title = "Select a file", filetypes=[("Image files", ["*.png", "*.jpg"])])
  if (not filename): return
  gl.set_state("mp_image")
  mpd.detect(filename)