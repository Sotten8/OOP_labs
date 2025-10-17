from editor import PointEditor, LineEditor, RectEditor, EllipseEditor

class ShapeObjectsEditor:
    def __init__(self, canvas, main_window=None):
        self._canvas = canvas
        self._main = main_window
        self._shapes = []
        self._current_editor = None

    def start_point_editor(self):
        self._current_editor = PointEditor(self._canvas)
    
    def start_line_editor(self):
        self._current_editor = LineEditor(self._canvas)
    
    def start_rect_editor(self):
        self._current_editor = RectEditor(self._canvas)
    
    def start_ellipse_editor(self):
        self._current_editor = EllipseEditor(self._canvas)

    def on_click(self, x, y):
        if self._current_editor:
            self._current_editor.on_click(x, y)

    def on_drag(self, x, y):
        if self._current_editor:
            self._current_editor.on_drag(x, y)
    
    def on_drop(self, x, y):
        if self._current_editor:
            shape = self._current_editor.on_drop(x, y)
            if shape:
                self._shapes.append(shape)
                self._redraw()
        return None
    
    def _redraw(self):
        self._canvas.delete("all")
        for shape in self._shapes:
            if shape:
                shape.show(self._canvas)