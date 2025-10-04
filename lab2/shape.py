from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
  
    def set(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
  
    @abstractmethod
    def show(self, canvas):
        pass

class PointShape(Shape):
    def show(self, canvas):
        canvas.create_oval(self._x1-1, self._y1-1, 
                          self._x1+1, self._y1+1, 
                          fill="black", outline="black")

class LineShape(Shape):
    def show(self, canvas):
        canvas.create_line(self._x1, self._y1, 
                          self._x2, self._y2, 
                          fill="black", width=1)

class RectShape(Shape):
    def __init__(self):
        super().__init__()
        self.__fill_color = "orange"
    
    def show(self, canvas):
        canvas.create_rectangle(self._x1, self._y1, 
                              self._x2, self._y2,
                              outline="black", fill=self.__fill_color, width=1)

class EllipseShape(Shape):
    def show(self, canvas):
        center_x = self._x1
        center_y = self._y1
        current_x = self._x2
        current_y = self._y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y
        
        canvas.create_oval(x1, y1, x2, y2, outline="black", width=1)