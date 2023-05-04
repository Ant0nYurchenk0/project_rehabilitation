import customtkinter as ck 
import tkinter as tk 


def add_label(frame: tk.Frame, x: int, y: int, name: str, 
              height:int =40, width:int =120, font: tuple[str, int] =("Arial", 20), text_color: str ="white", padx: int=10) -> ck.CTkLabel:
  new_label = ck.CTkLabel(frame, height=height, width=width, font=font, text_color=text_color, padx=padx)
  new_label.place(x=x, y=y)
  new_label.configure(text=name) 
  return new_label

def add_menu(root_menu: tk.Menu, label: str) -> tk.Menu:
  new_menu = tk.Menu(root_menu)
  root_menu.add_cascade(label= label, menu= new_menu)
  return new_menu

def add_command_to_menu(menu: tk.Menu, label: str, command) -> None:
  menu.add_command(label= label, command= command)

def add_frame(root: tk.Tk, x:int, y:int, bg: str, height: int, width: int) -> tk.Frame:
  new_frame = tk.Frame(root, width = width, height = height, bg = bg)
  new_frame.place(x=x, y=y)
  return new_frame