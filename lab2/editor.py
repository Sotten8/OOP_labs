from abc import ABC, abstractmethod
from shape import PointShape, LineShape, RectShape, EllipseShape

class Editor(ABC):
    @abstractmethod
    def on_click(self, x, y): pass
    
    @abstractmethod
    def on_drag(self, x, y): pass
    
    @abstractmethod
    def on_drop(self, x, y): pass

class ShapeEditor(Editor):
    def __init__(self, canvas):
        self._canvas = canvas
        self.__current_shape = None
        self.__preview_id = None
        self.__start_x = 0
        self.__start_y = 0
    
    def on_click(self, x, y):
        self.__start_x = x
        self.__start_y = y
    
    def on_drag(self, x, y):
        if self.__current_shape and self.__preview_id:
            self._canvas.delete(self.__preview_id)
            self.__current_shape.set(self.__start_x, self.__start_y, x, y)
            self.__preview_id = self._draw_preview()
    
    def on_drop(self, x, y):
        if self.__current_shape:
            self.__current_shape.set(self.__start_x, self.__start_y, x, y)
            if self.__preview_id:
                self._canvas.delete(self.__preview_id)
            shape = self.__current_shape
            self.__current_shape = None
            self.__preview_id = None
            return shape
        return None
    
    def on_menu_popup(self):
        print(f"Active editor: {self.get_menu_label()}")
    
    def _get_start_x(self):
        return self.__start_x
    
    def _get_start_y(self):
        return self.__start_y
    
    def _set_current_shape(self, shape):
        self.__current_shape = shape
    
    def _get_current_shape(self):
        return self.__current_shape
    
    def _set_preview_id(self, preview_id):
        self.__preview_id = preview_id
    
    def _get_preview_id(self):
        return self.__preview_id
    
    @abstractmethod
    def get_menu_label(self):
        pass

    @abstractmethod
    def _draw_preview(self):
        pass

class PointEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._set_current_shape(PointShape())
        self._get_current_shape().set(x, y, x, y)
        if self._get_preview_id():
            self._canvas.delete(self._get_preview_id())
        self._set_preview_id(self._draw_preview())
    
    def get_menu_label(self):
        return "Point"
    
    def _draw_preview(self):
        return self._canvas.create_oval(
            self._get_start_x()-2, self._get_start_y()-2,
            self._get_start_x()+2, self._get_start_y()+2,
            outline="blue", width=1
        )

class LineEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._set_current_shape(LineShape())
        self._get_current_shape().set(x, y, x, y)
        if self._get_preview_id():
            self._canvas.delete(self._get_preview_id())
        self._set_preview_id(self._draw_preview())
    
    def get_menu_label(self):
        return "Line"
    
    def _draw_preview(self):
        current_shape = self._get_current_shape()
        return self._canvas.create_line(
            self._get_start_x(), self._get_start_y(),
            current_shape._x2, current_shape._y2,
            fill="blue", width=1
        )

class RectEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._set_current_shape(RectShape())
        self._get_current_shape().set(x, y, x, y)
        if self._get_preview_id():
            self._canvas.delete(self._get_preview_id())
        self._set_preview_id(self._draw_preview())
    
    def get_menu_label(self):
        return "Rectangle"
    
    def _draw_preview(self):
        current_shape = self._get_current_shape()
        return self._canvas.create_rectangle(
            self._get_start_x(), self._get_start_y(),
            current_shape._x2, current_shape._y2,
            outline="blue", width=1
        )

class EllipseEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._set_current_shape(EllipseShape())
        self._get_current_shape().set(x, y, x, y)
        if self._get_preview_id():
            self._canvas.delete(self._get_preview_id())
        self._set_preview_id(self._draw_preview())
    
    def get_menu_label(self):
        return "Ellipse"
    
    def _draw_preview(self):
        center_x = self._get_start_x()
        center_y = self._get_start_y()
        current_shape = self._get_current_shape()
        current_x = current_shape._x2
        current_y = current_shape._y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y
        
        return self._canvas.create_oval(
            x1, y1, x2, y2,
            outline="blue", width=1
        )