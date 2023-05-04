from PIL import ImageTk 
import customtkinter as ck 

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