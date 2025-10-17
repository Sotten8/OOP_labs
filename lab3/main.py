import tkinter as tk
from tkinter import messagebox
from shape_objects_editor import ShapeObjectsEditor
from toolbar import Toolbar

class Main:
    def __init__(self):
        self._main_window = None
        self._canvas = None
        self._editor_manager = None
        self._current_mode = None
        self._menu_bar = None
        self._toolbar = None
        
    def run(self):
        self._create_window()
        self._create_canvas()
        self._create_editor()
        self._create_menu()
        self._create_toolbar()
        self._bind_events()
        self._set_default_editor()
        self._main_window.mainloop()
    
    def _create_window(self):
        self._main_window = tk.Tk()
        self._main_window.geometry("600x400+400+150")
        self._main_window.title("Lab3")
        self._main_window.resizable(False, False)
    
    def _create_canvas(self):
        self._canvas = tk.Canvas(self._main_window, width=600, height=400, bg="white")
        self._canvas.pack()
    
    def _create_editor(self):
        self._editor_manager = ShapeObjectsEditor(self._canvas, self._main_window)
    
    def _create_menu(self):
        self._current_mode = tk.StringVar(value="Point")
        self._menu_bar = tk.Menu(self._main_window)
        
        self._create_file_menu()
        self._create_objects_menu()
        self._create_help_menu()
        
        self._main_window.config(menu=self._menu_bar)
    
    def _create_file_menu(self):
        file_menu = tk.Menu(self._menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._main_window.quit)
        self._menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_toolbar(self):
        self._toolbar = Toolbar(self._main_window, self._canvas, self, self._current_mode)
        self._toolbar.create_toolbar()

    def _create_objects_menu(self):
        objects_menu = tk.Menu(self._menu_bar, tearoff=0)
        
        objects_menu.add_radiobutton(
            label="Крапка", 
            command=self.switch_to_point_mode,
            variable=self._current_mode, 
            value="Point"
        )
        objects_menu.add_radiobutton(
            label="Лінія", 
            command=self.switch_to_line_mode,
            variable=self._current_mode, 
            value="Line"
        )
        objects_menu.add_radiobutton(
            label="Прямокутник", 
            command=self.switch_to_rect_mode,
            variable=self._current_mode, 
            value="Rectangle"
        )
        objects_menu.add_radiobutton(
            label="Еліпс", 
            command=self.switch_to_ellipse_mode,
            variable=self._current_mode, 
            value="Ellipse"
        )
        
        self._menu_bar.add_cascade(label="Objects", menu=objects_menu)
    
    def _create_help_menu(self):
        help_menu = tk.Menu(self._menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_lab_information)
        self._menu_bar.add_cascade(label="Help", menu=help_menu)
    
    def switch_to_point_mode(self):
        self._editor_manager.start_point_editor()
        self._current_mode.set("Point")
        self._main_window.title(f"Lab3 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_line_mode(self):
        self._editor_manager.start_line_editor()
        self._current_mode.set("Line")
        self._main_window.title(f"Lab3 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_rect_mode(self):
        self._editor_manager.start_rect_editor()
        self._current_mode.set("Rectangle")
        self._main_window.title(f"Lab3 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_ellipse_mode(self):
        self._editor_manager.start_ellipse_editor()
        self._current_mode.set("Ellipse")
        self._main_window.title(f"Lab3 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def _show_lab_information(self):
        messagebox.showinfo("Info", "Lab 3 is working fine\n(c) Copyright 2025")
    
    def _bind_events(self):
        self._canvas.bind("<Button-1>", self._on_click)
        self._canvas.bind("<B1-Motion>", self._on_drag)
        self._canvas.bind("<ButtonRelease-1>", self._on_drop)
    
    def _on_click(self, event):
        self._editor_manager.on_click(event.x, event.y)
    
    def _on_drag(self, event):
        self._editor_manager.on_drag(event.x, event.y)
    
    def _on_drop(self, event):
        self._editor_manager.on_drop(event.x, event.y)
    
    def _set_default_editor(self):
        self.switch_to_point_mode()

if __name__ == "__main__":
    app = Main()
    app.run()