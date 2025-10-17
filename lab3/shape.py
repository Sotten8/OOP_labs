from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
  
    def set(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
  
    @abstractmethod
    def show(self, canvas):
        pass

class PointShape(Shape):
    def show(self, canvas):
        canvas.create_oval(self.x1-1, self.y1-1, 
                          self.x1+1, self.y1+1, 
                          fill="black", outline="black")

class LineShape(Shape):
    def show(self, canvas):
        canvas.create_line(self.x1, self.y1, 
                          self.x2, self.y2, 
                          fill="black", width=1)

class RectShape(Shape):
    def __init__(self):
        super().__init__()
        self._fill_color = "pink"
    
    def show(self, canvas):
        center_x = self.x1
        center_y = self.y1
        current_x = self.x2
        current_y = self.y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y
        
        canvas.create_rectangle(x1, y1, x2, y2,
                              outline="black", fill=self._fill_color, width=1)

class EllipseShape(Shape):
    def __init__(self):
        super().__init__()
        self._fill_color = "white"

    def show(self, canvas):
        canvas.create_oval(self.x1, self.y1, 
                          self.x2, self.y2, 
                          outline="black", fill=self._fill_color, width=1)