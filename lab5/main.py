import tkinter as tk
from tkinter import messagebox
from my_editor import MyEditor
from my_table import MyTable 
from table_view import TableView 
from shape import PointShape, LineShape, RectShape, EllipseShape, LineSegmentShape, CubeShape
from toolbar import Toolbar 


class Main:
    def __init__(self):
        self._main_window = None
        self._canvas = None
        self._current_mode = None
        self._menu_bar = None
        self._toolbar = None
        self._editor_manager = MyEditor.get_instance(canvas=None) 
        MyTable.get_instance()
        
    def run(self):
        self._create_window()
        self._create_canvas()
        
        MyEditor.get_instance()._canvas = self._canvas
        
        editor = MyEditor.get_instance()
        
        def table_reload_callback():
            table_instance = TableView.get_instance(self._main_window)
            if table_instance:
                table_instance.reload_data()
                table_instance._toplevel.update_idletasks() 
                table_instance._toplevel.lift()
        
        editor.register_gui_callback(table_reload_callback)

        MyTable.get_instance().register_listener(editor.handle_table_event)
        
        self._create_menu()
        self._create_toolbar()
        self._bind_events()
        self._set_default_mode()
        self._main_window.mainloop()
        
        TableView.destroy_window() 
    
    def _create_window(self):
        self._main_window = tk.Tk()
        self._main_window.geometry("800x600+100+100") 
        self._main_window.title("Lab5")
        self._main_window.bind('<Destroy>', self._on_exit)
        
    def _create_canvas(self):
        self._canvas = tk.Canvas(self._main_window, bg="white") 
        self._canvas.pack(fill="both", expand=True)
    
    def _create_menu(self):
        self._current_mode = tk.StringVar(value="Point")
        self._menu_bar = tk.Menu(self._main_window)
        
        self._create_file_menu()
        self._create_objects_menu()
        self._create_view_menu() 
        self._create_help_menu()
        
        self._main_window.config(menu=self._menu_bar)
    
    def _create_file_menu(self):
        file_menu = tk.Menu(self._menu_bar, tearoff=0)
        file_menu.add_command(label="Save to File", command=self._save_data)
        file_menu.add_command(label="Load from File", command=self._load_data) 
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._main_window.quit)
        self._menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_view_menu(self):
        view_menu = tk.Menu(self._menu_bar, tearoff=0)
        view_menu.add_command(label="Show/Hide Table", command=self._toggle_table_view)
        self._menu_bar.add_cascade(label="View", menu=view_menu)
        
    def _create_toolbar(self):
        self._toolbar = Toolbar(self._main_window, self._canvas, self, self._current_mode)
        self._toolbar.create_toolbar()

    def _create_objects_menu(self):
        objects_menu = tk.Menu(self._menu_bar, tearoff=0)
        
        objects_menu.add_radiobutton(label="Крапка", command=self.switch_to_point_mode, variable=self._current_mode, value="Point")
        objects_menu.add_radiobutton(label="Лінія", command=self.switch_to_line_mode, variable=self._current_mode, value="Line")
        objects_menu.add_radiobutton(label="Прямокутник", command=self.switch_to_rect_mode, variable=self._current_mode, value="Rectangle")
        objects_menu.add_radiobutton(label="Еліпс", command=self.switch_to_ellipse_mode, variable=self._current_mode, value="Ellipse")
        objects_menu.add_radiobutton(label="Відрізок", command=self.switch_to_line_segment_mode, variable=self._current_mode, value="Line Segment")
        objects_menu.add_radiobutton(label="Куб", command=self.switch_to_cube_mode, variable=self._current_mode, value="Cube")
        
        self._menu_bar.add_cascade(label="Objects", menu=objects_menu)
    
    def _create_help_menu(self):
        help_menu = tk.Menu(self._menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_lab_information)
        self._menu_bar.add_cascade(label="Help", menu=help_menu)
    
    def switch_to_point_mode(self):
        self._editor_manager.start(PointShape())
        self._current_mode.set("Point")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_line_mode(self):
        self._editor_manager.start(LineShape())
        self._current_mode.set("Line")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_rect_mode(self):
        self._editor_manager.start(RectShape())
        self._current_mode.set("Rectangle")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def switch_to_ellipse_mode(self):
        self._editor_manager.start(EllipseShape())
        self._current_mode.set("Ellipse")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()

    def switch_to_line_segment_mode(self):
        self._editor_manager.start(LineSegmentShape())
        self._current_mode.set("Line Segment")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()

    def switch_to_cube_mode(self):
        self._editor_manager.start(CubeShape())
        self._current_mode.set("Cube")
        self._main_window.title(f"Lab5 - {self._current_mode.get()} Mode")
        self._toolbar.update_button_states()
    
    def _show_lab_information(self):
        messagebox.showinfo("Info", "Lab 5 is working fine\n(c) Copyright 2025")
        
    def _save_data(self):
        path = "lab5/Lab5_objects.txt"
        filename = path.split('/')[-1]
        try:
            self._editor_manager.save_to_file(path)
            messagebox.showinfo("Save to File", f"Object data successfully saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
            
    def _load_data(self):
        path = "lab5/Lab5_objects.txt"
        filename = path.split('/')[-1]
        success = self._editor_manager.load_from_file(path)
        if success:
            messagebox.showinfo("Upload", f"Object are successfully loaded from {filename}!")
        else:
             messagebox.showerror("Error", f"File {filename} is not found or it has incorrect form.")


    def _toggle_table_view(self):
        if TableView._window_instance is None:
            TableView.get_instance(self._main_window)
        else:
            TableView.destroy_window()

    def _on_exit(self, event=None):
        TableView.destroy_window()
        
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
    
    def _set_default_mode(self):
        self.switch_to_point_mode()

if __name__ == "__main__":
    app = Main()
    app.run()