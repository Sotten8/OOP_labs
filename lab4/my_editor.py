class MyEditor:
    def __init__(self, canvas):
        self._canvas = canvas
        self._shapes = []
        self._current_shape = None
        self._preview_id = None
        self._start_x = 0
        self._start_y = 0

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
            self._current_shape.set(self._start_x, self._start_y, x, y)
            self._shapes.append(self._current_shape)
            self._clear_preview()
            self._current_shape.show(self._canvas)
            self._current_shape = type(self._current_shape)()

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

    def _redraw(self):
        self._canvas.delete("all")
        for shape in self._shapes:
            shape.show(self._canvas)