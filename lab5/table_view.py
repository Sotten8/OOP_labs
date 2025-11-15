import tkinter as tk
from tkinter import ttk
from my_table import MyTable, EVENT_SELECT, EVENT_DELETE

class TableView:
    _window_instance = None

    @staticmethod
    def get_instance(root=None):
        if TableView._window_instance is None:
            if root is None:
                pass
            TableView._window_instance = TableView(root)
            MyTable.get_instance().set_view(TableView._window_instance) 
        return TableView._window_instance

    @staticmethod
    def destroy_window():
        if TableView._window_instance:
            MyTable.get_instance().set_view(None)
            TableView._window_instance._toplevel.destroy()
            TableView._window_instance = None

    def __init__(self, root):
        self._toplevel = tk.Toplevel(root) 
        self._toplevel.title("Objects table")
        self._toplevel.geometry("500x350")
        self._toplevel.protocol("WM_DELETE_WINDOW", self.destroy_window) 
        
        self._tree = self._create_table_widget()
        self._create_controls() 
        self._load_initial_data()
        
    def _create_table_widget(self):
        columns = ("Назва", "X1", "Y1", "X2", "Y2")
        tree = ttk.Treeview(self._toplevel, columns=columns, show="headings") 
        
        for col in columns:
            tree.heading(col, text=col)
            width = 75 if col != "Name" else 120
            tree.column(col, anchor="center", width=width)

        vsb = ttk.Scrollbar(self._toplevel, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        
        vsb.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)
        
        tree.bind("<<TreeviewSelect>>", self._on_select_item)

        return tree
    
    def _create_controls(self):
        frame = tk.Frame(self._toplevel)
        frame.pack(fill="x", pady=5, padx=5)

        delete_btn = tk.Button(frame, text="Delete object", command=self._on_delete_item)
        delete_btn.pack(side="bottom", padx=5)

    def _on_select_item(self, event):
        selected_items = self._tree.selection()
        if selected_items:
            item_id = selected_items[0]
            index = int(self._tree.item(item_id, "text")) 
            
            MyTable.get_instance().notify_listeners(EVENT_SELECT, index)
        else:
             MyTable.get_instance().notify_listeners(EVENT_SELECT, -1) 

    def _on_delete_item(self):
        selected_items = self._tree.selection()
        if selected_items:
            item_id = selected_items[0]
            index = int(self._tree.item(item_id, "text")) 
            
            MyTable.get_instance().notify_listeners(EVENT_DELETE, index)
            
    def _load_initial_data(self):
        self.reload_data()

    def reload_data(self):
        try:
            self._tree.selection_remove(self._tree.selection())
        except:
             pass 
        
        self.clear_table() 
        
        data = MyTable.get_instance().get_data()
        for index, shape in enumerate(data):
            self.insert_row(shape, index)
            
    def insert_row(self, shape, index):
        self._tree.insert("", "end", text=str(index), 
                          values=(shape.__class__.__name__, 
                                  shape.x1, shape.y1, 
                                  shape.x2, shape.y2))
                                  
    def clear_table(self):
        for item in self._tree.get_children():
            self._tree.delete(item)