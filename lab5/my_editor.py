from my_table import MyTable, EVENT_SELECT, EVENT_DELETE 
from shape import CLASS_MAP 

class MyEditor:
    _instance = None
    
    def __init__(self, canvas=None):
        if MyEditor._instance is not None:
            raise Exception("This is Singleton! Use MyEditor.get_instance()")

        self._canvas = canvas
        self._shapes = []
        self._current_shape = None
        self._preview_id = None
        self._start_x = 0
        self._start_y = 0
        self._highlight_id = None
        self._gui_reload_callback = None
        MyEditor._instance = self

    @staticmethod
    def get_instance(canvas=None):
        if MyEditor._instance is None:
            MyEditor(canvas)
        return MyEditor._instance
    
    def register_gui_callback(self, callback):
        self._gui_reload_callback = callback
    
    def start(self, shape):
        self._current_shape = shape

    def on_click(self, x, y):
        self._start_x = x
        self._start_y = y
        if self._current_shape:
            self._current_shape.set(x, y, x, y)
            self._draw_preview()

    def on_drag(self, x, y):
        if self._current_shape:
            self._current_shape.set(self._start_x, self._start_y, x, y)
            self._update_preview()

    def on_drop(self, x, y):
        if self._current_shape:
            new_shape = type(self._current_shape)()
            new_shape.set(self._start_x, self._start_y, x, y)
            
            self._shapes.append(new_shape)
            
            MyTable.get_instance().add_shape(new_shape) 

            self._clear_preview() 
            self._redraw()
            self._current_shape = type(self._current_shape)()

    def _redraw(self):
        self._canvas.delete("all")
        self._highlight_id = None
        for shape in self._shapes:
            shape.show(self._canvas)
            
    def _draw_preview(self):
        if self._current_shape and not self._preview_id:
            preview_result = self._current_shape.show_preview(self._canvas)
            if isinstance(preview_result, list):
                self._preview_id = preview_result
            else:
                self._preview_id = [preview_result]

    def _update_preview(self):
        if self._current_shape:
            self._clear_preview()
            self._draw_preview()

    def _clear_preview(self):
        if self._preview_id:
            for preview_id in self._preview_id:
                self._canvas.delete(preview_id)
            self._preview_id = None

    def _highlight_shape(self, index):
        if self._highlight_id:
            self._canvas.delete(self._highlight_id)
            self._highlight_id = None
        
        if 0 <= index < len(self._shapes):
            shape_to_highlight = self._shapes[index]
            
            min_x, min_y, max_x, max_y = shape_to_highlight.get_bounding_box() 
            
            padding = 5
            self._highlight_id = self._canvas.create_rectangle(
                min_x - padding, min_y - padding, 
                max_x + padding, max_y + padding, 
                outline="red", width=2, dash=(4, 4)
            )

    def _delete_shape(self, index):
        if 0 <= index < len(self._shapes):
            
            self._shapes.pop(index)
            try:
                 MyTable.get_instance().get_data().pop(index) 
            except IndexError:
                 pass
            
            self._redraw() 
            
            if self._gui_reload_callback:
                self._gui_reload_callback()
            
            self._highlight_shape(-1)

    def handle_table_event(self, event_type, index):
        if event_type == EVENT_SELECT:
            self._highlight_shape(index)
        elif event_type == EVENT_DELETE:
            self._delete_shape(index)

    def save_to_file(self, path="lab5/Lab5_objects.txt"):
        with open(path, 'w') as f:
            for shape in self._shapes:
                class_name = type(shape).__name__
                line = f"{class_name}\t{shape.x1}\t{shape.y1}\t{shape.x2}\t{shape.y2}\n"
                f.write(line)
        return True
        
    def load_from_file(self, path="lab5/Lab5_objects.txt"):        
        self._shapes.clear()
        MyTable.get_instance().get_data().clear()
        
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                        
                    parts = line.split('\t')
                    if len(parts) != 5:
                        continue
                        
                    class_name = parts[0]
                    coords = [int(p) for p in parts[1:]]
                    
                    if class_name in CLASS_MAP:
                        ShapeClass = CLASS_MAP[class_name]
                        new_shape = ShapeClass()
                        new_shape.set(*coords)
                        
                        self._shapes.append(new_shape)
                        MyTable.get_instance().add_shape(new_shape)
                        
            self._redraw() 
            if self._gui_reload_callback:
                self._gui_reload_callback()
                
            return True
            
        except FileNotFoundError:
            return False
        except Exception:
            return False