from PIL import Image, ImageDraw, ImageTk

class BitmapFactory:
    def __init__(self):
        self._images = {}

    def create_toolbar_bitmaps(self, size=28):
        center = size // 2

        self._images["Крапка"] = self._create_point_bitmap(size, center)
        self._images["Лінія"] = self._create_line_bitmap(size, center)
        self._images["Прямокутник"] = self._create_rectangle_bitmap(size, center)
        self._images["Еліпс"] = self._create_ellipse_bitmap(size, center)
        self._images["Відрізок"] = self._create_line_segment_bitmap(size, center)
        self._images["Куб"] = self._create_cube_bitmap(size, center)

        return self._images
  
    def _create_point_bitmap(self, size, center):
        point_img = Image.new("RGB", (size, size), "white")
        point_draw = ImageDraw.Draw(point_img)

        point_draw.ellipse([center-4, center-4, center+4, center+4], 
                           fill="black", outline="black", width=1)
        return ImageTk.PhotoImage(point_img)
  
    def _create_line_bitmap(self, size, center):
        line_img = Image.new("RGB", (size, size), "white")
        line_draw = ImageDraw.Draw(line_img)

        line_draw.line([center-7, center+7, center+7, center-7], 
                       fill="black", width=2)
        return ImageTk.PhotoImage(line_img)
  
    def _create_rectangle_bitmap(self, size, center):
        rectangle_img = Image.new("RGB", (size, size), "white")
        rectangle_draw = ImageDraw.Draw(rectangle_img)

        rectangle_draw.rectangle([center-7, center-4, center+7, center+6], 
                       fill="black", outline="black", width=1)
        return ImageTk.PhotoImage(rectangle_img)
  
    def _create_ellipse_bitmap(self, size, center):
        ellipse_img = Image.new("RGB", (size, size), "white")
        ellipse_draw = ImageDraw.Draw(ellipse_img)

        ellipse_draw.ellipse([center-7, center-4, center+7, center+4], 
                       fill="black", outline="black", width=1)
        return ImageTk.PhotoImage(ellipse_img)
    
    def _create_line_segment_bitmap(self, size, center):
        line_segment_img = Image.new("RGB", (size, size), "white")
        line_segment_draw = ImageDraw.Draw(line_segment_img)

        line_segment_draw.ellipse([center-9, center+3, center-3, center+9], fill="white", outline="black", width=2)
        line_segment_draw.line([center-4, center+4, center+6, center-6], 
                       fill="black", width=2)
        line_segment_draw.ellipse([center+3, center-9, center+9, center-3], fill="white", outline="black", width=2)
        return ImageTk.PhotoImage(line_segment_img)
    
    def _create_cube_bitmap(self, size, center):
        cube_img = Image.new("RGB", (size, size), "white")
        cube_draw = ImageDraw.Draw(cube_img)
        
        cube_draw.rectangle([center-6, center-4, center+2, center+4], outline="black", width=1)
        cube_draw.rectangle([center-2, center-6, center+6, center+2], outline="black", width=1)
        cube_draw.line([center-6, center-4, center-2, center-6], fill="black", width=1)
        cube_draw.line([center+2, center-4, center+6, center-6], fill="black", width=1)
        cube_draw.line([center-6, center+4, center-2, center+2], fill="black", width=1)
        cube_draw.line([center+2, center+4, center+6, center+2], fill="black", width=1)
        
        return ImageTk.PhotoImage(cube_img)
    
    def get_image(self, name):
        return self._images.get(name)
  
    def get_all_images(self):
        return self._images