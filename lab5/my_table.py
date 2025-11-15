class MyTable:
    _instance = None
    
    def __init__(self):
        if MyTable._instance is not None:
            raise Exception("This is Singleton! Use MyEditor.get_instance()")

        self._data = [] 
        self._view = None 
        self._listeners = [] 
        MyTable._instance = self

    @staticmethod
    def get_instance():
        if MyTable._instance is None:
            MyTable()
        return MyTable._instance

    def set_view(self, view):
        self._view = view
            
    def get_data(self):
        return self._data
        
    def add_shape(self, shape):
        self._data.append(shape)
        new_index = len(self._data) - 1 
        
        if self._view:
            self._view.insert_row(shape, new_index)
            
        return new_index

    def register_listener(self, listener_callback):
        self._listeners.append(listener_callback)

    def notify_listeners(self, event_type, index):
        for callback in self._listeners:
            callback(event_type, index)

EVENT_SELECT = "select"
EVENT_DELETE = "delete"