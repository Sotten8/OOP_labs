import tkinter as tk
from tkinter import messagebox
from shape_objects_editor import ShapeObjectsEditor

main = tk.Tk()
main.geometry("600x400+400+150")
main.title("Lab2")
main.resizable(False, False)

canvas = tk.Canvas(main, width=600, height=400, bg="white")
canvas.pack()

editor_manager = ShapeObjectsEditor(canvas)

def on_click(event):
    editor_manager.on_click(event.x, event.y)

def on_drag(event):
    editor_manager.on_drag(event.x, event.y)

def on_drop(event):
    editor_manager.on_drop(event.x, event.y)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_drop)

def show_lab_information():
    messagebox.showinfo("Info", "Lab 2 is working fine\n(c) Copyright 2025")

current_mode = tk.StringVar(value="Point")

def set_point_editor():
    editor_manager.start_point_editor()
    current_mode.set("Point")
    editor_manager.on_menu_popup()
    main.title("Lab2 - Point Mode")

def set_line_editor():
    editor_manager.start_line_editor()
    current_mode.set("Line")
    editor_manager.on_menu_popup()
    main.title("Lab2 - Line Mode")

def set_rect_editor():
    editor_manager.start_rect_editor()
    current_mode.set("Rectangle")
    editor_manager.on_menu_popup()
    main.title("Lab2 - Rectangle Mode")

def set_ellipse_editor():
    editor_manager.start_ellipse_editor()
    current_mode.set("Ellipse")
    editor_manager.on_menu_popup()
    main.title("Lab2 - Ellipse Mode")

menu_bar = tk.Menu(main)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=main.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

objects_menu = tk.Menu(menu_bar, tearoff=0)
objects_menu.add_radiobutton(label="Крапка", command=set_point_editor, variable=current_mode, value="Point")
objects_menu.add_radiobutton(label="Лінія", command=set_line_editor, variable=current_mode, value="Line")
objects_menu.add_radiobutton(label="Прямокутник", command=set_rect_editor, variable=current_mode, value="Rectangle")
objects_menu.add_radiobutton(label="Еліпс", command=set_ellipse_editor, variable=current_mode, value="Ellipse")
menu_bar.add_cascade(label="Objects", menu=objects_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_lab_information)
menu_bar.add_cascade(label="Help", menu=help_menu)

main.config(menu=menu_bar)

set_point_editor()

main.mainloop()