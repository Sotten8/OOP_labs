from editor import PointEditor, LineEditor, RectEditor, EllipseEditor

class ShapeObjectsEditor:
    def __init__(self, canvas):
        self._canvas = canvas
        self.__shapes = [None] * 122
        self.__shapes_count = 0
        self.__current_editor = None

    def start_point_editor(self):
        self.__current_editor = PointEditor(self._canvas)
    
    def start_line_editor(self):
        self.__current_editor = LineEditor(self._canvas)
    
    def start_rect_editor(self):
        self.__current_editor = RectEditor(self._canvas)
    
    def start_ellipse_editor(self):
        self.__current_editor = EllipseEditor(self._canvas)

    def on_click(self, x, y):
        if self.__current_editor:
            self.__current_editor.on_click(x, y)
    
    def on_drop(self, x, y):
        if self.__current_editor:
            shape = self.__current_editor.on_drop(x, y)
            if shape and self.__shapes_count < len(self.__shapes) - 1:
                self.__shapes[self.__shapes_count] = shape
                self.__shapes_count += 1
                self._redraw()
        return None
    
    def on_drag(self, x, y):
        if self.__current_editor:
            self.__current_editor.on_drag(x, y)
    
    def _redraw(self):
        for i in range(self.__shapes_count):
            if self.__shapes[i]:
                self.__shapes[i].show(self._canvas)
    
    def on_menu_popup(self):
        self.__current_editor.on_menu_popup()