import tkinter as tk
from tkinter import messagebox
from shape_objects_editor import ShapeObjectsEditor

class Main:
    def __init__(self):
        self.main_window = None
        self.canvas = None
        self.editor_manager = None
        self.current_mode = None
        self.menu_bar = None
        
    def run(self):
        self._create_window()
        self._create_canvas()
        self._create_editor()
        self._create_menu()
        self._bind_events()
        self._set_default_editor()
        self.main_window.mainloop()
    
    def _create_window(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("600x400+400+150")
        self.main_window.title("Lab2")
        self.main_window.resizable(False, False)
    
    def _create_canvas(self):
        self.canvas = tk.Canvas(self.main_window, width=600, height=400, bg="white")
        self.canvas.pack()
    
    def _create_editor(self):
        self.editor_manager = ShapeObjectsEditor(self.canvas, self.main_window)
    
    def _create_menu(self):
        self.current_mode = tk.StringVar(value="Point")
        self.menu_bar = tk.Menu(self.main_window)
        
        self._create_file_menu()
        self._create_objects_menu()
        self._create_help_menu()
        
        self.main_window.config(menu=self.menu_bar)
    
    def _create_file_menu(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.main_window.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
    
    def _create_objects_menu(self):
        objects_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        objects_menu.add_radiobutton(
            label="Крапка", 
            command=self._set_point_editor, 
            variable=self.current_mode, 
            value="Point"
        )
        objects_menu.add_radiobutton(
            label="Лінія", 
            command=self._set_line_editor, 
            variable=self.current_mode, 
            value="Line"
        )
        objects_menu.add_radiobutton(
            label="Прямокутник", 
            command=self._set_rect_editor, 
            variable=self.current_mode, 
            value="Rectangle"
        )
        objects_menu.add_radiobutton(
            label="Еліпс", 
            command=self._set_ellipse_editor, 
            variable=self.current_mode, 
            value="Ellipse"
        )
        
        self.menu_bar.add_cascade(label="Objects", menu=objects_menu)
    
    def _create_help_menu(self):
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_lab_information)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
    
    def _set_point_editor(self):
        self.editor_manager.start_point_editor()
        self.current_mode.set("Point")
        self.editor_manager.on_menu_popup()
        self.main_window.title("Lab2 - Point Mode")
    
    def _set_line_editor(self):
        self.editor_manager.start_line_editor()
        self.current_mode.set("Line")
        self.editor_manager.on_menu_popup()
        self.main_window.title("Lab2 - Line Mode")
    
    def _set_rect_editor(self):
        self.editor_manager.start_rect_editor()
        self.current_mode.set("Rectangle")
        self.editor_manager.on_menu_popup()
        self.main_window.title("Lab2 - Rectangle Mode")
    
    def _set_ellipse_editor(self):
        self.editor_manager.start_ellipse_editor()
        self.current_mode.set("Ellipse")
        self.editor_manager.on_menu_popup()
        self.main_window.title("Lab2 - Ellipse Mode")
    
    def _show_lab_information(self):
        messagebox.showinfo("Info", "Lab 2 is working fine\n(c) Copyright 2025")
    
    def _bind_events(self):
        self.canvas.bind("<Button-1>", self._on_click)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_drop)
    
    def _on_click(self, event):
        self.editor_manager.on_click(event.x, event.y)
    
    def _on_drag(self, event):
        self.editor_manager.on_drag(event.x, event.y)
    
    def _on_drop(self, event):
        self.editor_manager.on_drop(event.x, event.y)
    
    def _set_default_editor(self):
        self._set_point_editor()


if __name__ == "__main__":
    app = Main()
    app.run()