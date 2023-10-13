from PIL import ImageTk 
import customtkinter as ck 
from datetime import timedelta

labels = {}

def add_label(name: str, label: ck.CTkLabel):
  global labels
  labels[name] = label

def set_text(name: str, text: str):
  labels[name].configure(text = text)

def set_image(name: str, imgtk: ImageTk.PhotoImage):
  global labels
  labels[name].imgtk = imgtk 
  labels[name].configure(image=imgtk)
  labels[name].update()

def update_timer_label(name: str, start_time = None, elapsed_time=None, total_duration = None):
    if elapsed_time is not None:
        elapsed_time_str = str(timedelta(seconds=elapsed_time))
        total_duration_str = str(timedelta(seconds=total_duration))
        labels[name].config(text=f'{elapsed_time_str} / {total_duration_str}')
    else:
        labels[name].config(text=' 00:00:00 / 00:00:00')
