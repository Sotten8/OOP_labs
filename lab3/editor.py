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
        self._current_shape = None
        self._preview_id = None
        self._start_x = 0
        self._start_y = 0
    
    def on_click(self, x, y):
        self._start_x = x
        self._start_y = y
    
    def on_drag(self, x, y):
        if self._current_shape and self._preview_id:
            self._canvas.delete(self._preview_id)
            self._current_shape.set(self._start_x, self._start_y, x, y)
            self._preview_id = self._draw_preview()
    
    def on_drop(self, x, y):
        if self._current_shape:
            self._current_shape.set(self._start_x, self._start_y, x, y)
            if self._preview_id:
                self._canvas.delete(self._preview_id)
            shape = self._current_shape
            self._current_shape = None
            self._preview_id = None
            return shape
        return None
    
    @abstractmethod
    def _draw_preview(self):
        pass

class PointEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._current_shape = PointShape()
        self._current_shape.set(x, y, x, y)
        if self._preview_id:
            self._canvas.delete(self._preview_id)
        self._preview_id = self._draw_preview()
    
    def _draw_preview(self):
        return self._canvas.create_oval(
            self._start_x-2, self._start_y-2,
            self._start_x+2, self._start_y+2,
            outline="red", width=1
        )

class LineEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._current_shape = LineShape()
        self._current_shape.set(x, y, x, y)
        if self._preview_id:
            self._canvas.delete(self._preview_id)
        self._preview_id = self._draw_preview()
    
    def _draw_preview(self):
        current_shape = self._current_shape
        return self._canvas.create_line(
            self._start_x, self._start_y,
            current_shape.x2, current_shape.y2,
            fill="red", width=1
        )

class RectEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._current_shape = RectShape()
        self._current_shape.set(x, y, x, y)
        if self._preview_id:
            self._canvas.delete(self._preview_id)
        self._preview_id = self._draw_preview()

    def _draw_preview(self):
        center_x = self._start_x
        center_y = self._start_y
        current_shape = self._current_shape
        current_x = current_shape.x2
        current_y = current_shape.y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y
        
        return self._canvas.create_rectangle(
            x1, y1, x2, y2,
            outline="red", width=1
        )

class EllipseEditor(ShapeEditor):
    def on_click(self, x, y):
        super().on_click(x, y)
        self._current_shape = EllipseShape()
        self._current_shape.set(x, y, x, y)
        if self._preview_id:
            self._canvas.delete(self._preview_id)
        self._preview_id = self._draw_preview()
    
    def _draw_preview(self):
        current_shape = self._current_shape
        return self._canvas.create_oval(
            self._start_x, self._start_y,
            current_shape.x2, current_shape.y2,
            outline="red", width=1
        )