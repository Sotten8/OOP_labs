import tkinter as tk
from tkinter import messagebox
from module1 import first_window
from module2 import second_window
from module3 import third_window

main = tk.Tk()
main.geometry("600x400+400+150")
main.title("Lab1")
main.resizable(False, False)

def show_lab_information():
  messagebox.showinfo("Info", "Lab 1 is working fine\n(c) Copyright 2025")

def open_first_window(prev_window=None):
  if prev_window:
    prev_window.destroy()
  first_window(main, next_callback=open_second_window)  

def open_second_window(prev_window=None):
  if prev_window:
    prev_window.destroy()
  second_window(main, back_callback=open_first_window)  

group_label = tk.Label(main, text="", font=("Times New Roman", 20))
group_label.pack(expand=True)

menu_bar = tk.Menu(main)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=main.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_lab_information)
menu_bar.add_cascade(label="Help", menu=help_menu)

work_menu = tk.Menu(menu_bar, tearoff=0)
work_menu.add_command(label="Робота 1", command=open_first_window)
work_menu.add_command(label="Робота 2", command=lambda: third_window(main, group_label))
menu_bar.add_cascade(label="Work", menu=work_menu)

main.config(menu=menu_bar)

main.mainloop()
