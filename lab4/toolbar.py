import tkinter as tk
from bitmap_factory import BitmapFactory

class Toolbar:
    def __init__(self, main_window, canvas, main_app, current_mode):
        self._main_window = main_window
        self._canvas = canvas
        self._main_app = main_app
        self._current_mode = current_mode
        self._bitmap_factory = BitmapFactory()
        self._tool_buttons = {}
        self._tooltip_window = None
        self._toolbar_frame = None
        
    def create_toolbar(self):
        self._toolbar_frame = tk.Frame(self._main_window, bg="lightgray", height=42)
        self._toolbar_frame.pack(fill="x", side="top", before=self._canvas)
        self._toolbar_frame.pack_propagate(False)

        images = self._bitmap_factory.create_toolbar_bitmaps()

        tools = [
            ("Крапка", self._main_app.switch_to_point_mode, "Намалювати крапку"),
            ("Лінія", self._main_app.switch_to_line_mode, "Намалювати лінію"),
            ("Прямокутник", self._main_app.switch_to_rect_mode, "Намалювати прямокутник"),
            ("Еліпс", self._main_app.switch_to_ellipse_mode, "Намалювати еліпс"),
            ("Відрізок", self._main_app.switch_to_line_segment_mode, "Намалювати відрізок"),
            ("Куб", self._main_app.switch_to_cube_mode, "Намалювати куб")
        ]

        for i, (name, command, tooltip) in enumerate(tools):
            button = tk.Button(
                self._toolbar_frame,
                image=images[name],
                command=command,
                relief="raised",
                bg="lightblue",
                width=30,
                height=30
            )

            button.pack(side="left", padx=2, pady=2)
            self._tool_buttons[name] = button

            self._create_tooltip(button, tooltip, i)
    
    def _create_tooltip(self, widget, description, button_index):
        def show_tooltip(event):
            if self._tooltip_window:
                self._tooltip_window.destroy()
            
            self._tooltip_window = tk.Toplevel(self._main_window)
            self._tooltip_window.wm_overrideredirect(True)
            
            base_x = self._main_window.winfo_rootx() + 10
            base_y = self._main_window.winfo_rooty() + 45
            
            screen_width = self._main_window.winfo_screenwidth()
            tooltip_x = min(base_x + (button_index * 35), screen_width - 200)
            tooltip_y = base_y
            
            self._tooltip_window.wm_geometry(f"+{tooltip_x}+{tooltip_y}")

            label = tk.Label(self._tooltip_window, text=description,
                             bg="lightyellow",
                             relief="solid",
                             borderwidth=1,
                             font=("Arial", 9),
                             padx=4, pady=2)
            label.pack()

        def hide_tooltip(event):
            if self._tooltip_window:
                self._tooltip_window.destroy()
                self._tooltip_window = None

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)
        widget.bind("<ButtonPress>", hide_tooltip)
    
    def _update_button_states(self):
        mode_mapping = {
            "Point": "Крапка",
            "Line": "Лінія", 
            "Rectangle": "Прямокутник",
            "Ellipse": "Еліпс",
            "Line Segment": "Відрізок",
            "Cube": "Куб"
        }
        
        current_button_name = mode_mapping.get(self._current_mode.get())
        
        for name, button in self._tool_buttons.items():
            if name == current_button_name:
                button.config(relief="sunken", bg="lightgreen")
            else:
                button.config(relief="raised", bg="lightblue")

    def update_button_states(self):
        self._update_button_states()