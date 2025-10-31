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

    @abstractmethod
    def show_preview(self, canvas):
        pass


class PointShape(Shape):
    def show(self, canvas):
        canvas.create_oval(self.x1-2, self.y1-2,
                            self.x1+2, self.y1+2,
                            fill="black", outline="black")

    def show_preview(self, canvas):
        return canvas.create_oval(
            self.x1-3, self.y1-3, self.x1+3, self.y1+3, outline="red", dash=(4, 2))

class LineShape(Shape):
    def show(self, canvas, fill_color="black", width=2):
        canvas.create_line(self.x1, self.y1,
                            self.x2, self.y2,
                            fill=fill_color, width=width)

    def show_preview(self, canvas, fill_color="red", width=2, dash=(4, 2)):
        return canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill=fill_color, width=width, dash=dash)

class RectShape(Shape):
    def __init__(self):
        super().__init__()
        self._fill_color = "pink"

    def show(self, canvas, outline_color="black", width=2, fill_color=None):
        fill = fill_color if fill_color is not None else self._fill_color
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                              outline=outline_color, fill=fill, width=width)

    def show_preview(self, canvas, outline_color="red", width=2, dash=(4, 2)):
        return canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                     outline=outline_color, width=width, dash=dash)

class EllipseShape(Shape):
    def __init__(self):
        super().__init__()
        self._fill_color = "white"

    def show(self, canvas, outline_color="black", width=2, fill_color=None):
        center_x = self.x1
        center_y = self.y1
        current_x = self.x2
        current_y = self.y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y
        
        fill = fill_color if fill_color is not None else self._fill_color

        canvas.create_oval(x1, y1,
                            x2, y2,
                            outline=outline_color, fill=fill, width=width)

    def show_preview(self, canvas, outline_color="red", width=2, dash=(4, 2)):
        center_x = self.x1
        center_y = self.y1
        current_x = self.x2
        current_y = self.y2
        
        x1 = 2 * center_x - current_x
        y1 = 2 * center_y - current_y
        x2 = current_x
        y2 = current_y

        return canvas.create_oval(x1, y1, x2, y2,
                                 outline=outline_color, width=width, dash=dash)


class LineSegmentShape(LineShape, EllipseShape):
    def __init__(self):
        LineShape.__init__(self) 
        EllipseShape.__init__(self) 
        self._line_color = "black"
        self._radius = 3

    def _calculate_ellipses(self):
        ellipse1_coords = (self.x1 - self._radius, self.y1 - self._radius, self.x1 + self._radius, self.y1 + self._radius)
        ellipse2_coords = (self.x2 - self._radius, self.y2 - self._radius, self.x2 + self._radius, self.y2 + self._radius)
        return ellipse1_coords, ellipse2_coords

    def show(self, canvas):
        original_coords = (self.x1, self.y1, self.x2, self.y2)

        LineShape.show(self, canvas, fill_color=self._line_color)
        
        ellipse1_coords, ellipse2_coords = self._calculate_ellipses()
        
        temp_ellipse = EllipseShape()
        
        x1_o, y1_o, x2_o, y2_o = ellipse1_coords
        center_x_1 = (x1_o + x2_o) / 2
        center_y_1 = (y1_o + y2_o) / 2
        temp_ellipse.set(center_x_1, center_y_1, x2_o, y2_o)
        temp_ellipse.show(canvas, outline_color=self._line_color, fill_color="white") 

        x1_o, y1_o, x2_o, y2_o = ellipse2_coords
        center_x_2 = (x1_o + x2_o) / 2
        center_y_2 = (y1_o + y2_o) / 2
        temp_ellipse.set(center_x_2, center_y_2, x2_o, y2_o)
        temp_ellipse.show(canvas, outline_color=self._line_color, fill_color="white")
        
        self.set(*original_coords)
        
    def show_preview(self, canvas):
        preview_ids = []
        original_coords = (self.x1, self.y1, self.x2, self.y2)
        
        line_id = LineShape.show_preview(self, canvas, fill_color="red")
        preview_ids.append(line_id)
        
        ellipse1_coords, ellipse2_coords = self._calculate_ellipses()

        temp_ellipse = EllipseShape()
        
        x1_o, y1_o, x2_o, y2_o = ellipse1_coords
        center_x_1 = (x1_o + x2_o) / 2
        center_y_1 = (y1_o + y2_o) / 2
        temp_ellipse.set(center_x_1, center_y_1, x2_o, y2_o)
        preview_ids.append(temp_ellipse.show_preview(canvas, outline_color="red"))

        x1_o, y1_o, x2_o, y2_o = ellipse2_coords
        center_x_2 = (x1_o + x2_o) / 2
        center_y_2 = (y1_o + y2_o) / 2
        temp_ellipse.set(center_x_2, center_y_2, x2_o, y2_o)
        preview_ids.append(temp_ellipse.show_preview(canvas, outline_color="red"))
        
        self.set(*original_coords)
        
        return preview_ids

class CubeShape(LineShape, RectShape):
    def __init__(self):
        LineShape.__init__(self)
        RectShape.__init__(self)
        self._cube_color = "black"
        self._depth_ratio = 0.3

    def _calculate_cube_points(self):
        x1_start, y1_start = min(self.x1, self.x2), min(self.y1, self.y2)
        x2_end, y2_end = max(self.x1, self.x2), max(self.y1, self.y2)

        width = x2_end - x1_start
        height = y2_end - y1_start
        depth = int(min(width, height) * self._depth_ratio)
        
        front_face_coords = (x1_start, y1_start, x2_end, y2_end)
        
        x1_back = x1_start + depth
        y1_back = y1_start - depth
        x2_back = x2_end + depth
        y2_back = y2_end - depth

        edges = [
            (x1_back, y1_back, x2_back, y1_back),
            (x2_back, y1_back, x2_back, y2_back),
            (x2_back, y2_back, x1_back, y2_back),
            (x1_back, y2_back, x1_back, y1_back),
            
            (x1_start, y1_start, x1_back, y1_back), 
            (x2_end, y1_start, x2_back, y1_back),
            (x2_end, y2_end, x2_back, y2_back), 
            (x1_start, y2_end, x1_back, y2_back)
            
        ]
        return front_face_coords, edges

    def show(self, canvas):
        front_face_coords, edges = self._calculate_cube_points()
        original_coords = (self.x1, self.y1, self.x2, self.y2)

        for edge in edges:
            self.set(edge[0], edge[1], edge[2], edge[3])
            LineShape.show(self, canvas, fill_color=self._cube_color)
            
        temp_rect = RectShape()
        temp_rect.set(*front_face_coords)
        temp_rect.show(canvas, outline_color=self._cube_color, fill_color="")
            
        self.set(*original_coords)

    def show_preview(self, canvas):
        preview_ids = []
        front_face_coords, edges = self._calculate_cube_points()
        original_coords = (self.x1, self.y1, self.x2, self.y2)
        
        for edge in edges:
            self.set(edge[0], edge[1], edge[2], edge[3])
            preview_ids.append(LineShape.show_preview(self, canvas, fill_color="red"))
        
        temp_rect = RectShape()
        temp_rect.set(*front_face_coords)
        preview_ids.append(temp_rect.show_preview(canvas, outline_color="red"))
        
        self.set(*original_coords)

        return preview_ids
