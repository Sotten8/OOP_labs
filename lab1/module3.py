import tkinter as tk

def third_window(master, master_label):
  master_label.config(text="")
  work2_window = tk.Toplevel(master)
  work2_window.geometry("300x250+550+250")
  work2_window.title("Group list")
  work2_window.resizable(False, False)

  top_frame = tk.Frame(work2_window)
  top_frame.pack(fill="both", expand=True, padx=5, pady=5)
  bottom_frame = tk.Frame(work2_window)
  bottom_frame.pack(side="bottom", pady=10)

  scrollbar = tk.Scrollbar(top_frame)
  scrollbar.pack(side="right", fill="y")

  group_list = tk.Listbox(top_frame, yscrollcommand=scrollbar.set, bg="#d3d3d3")
  group_list.pack(side="left", fill="both", expand=True)

  def on_select(listbox, cur_window, label):
    choice = listbox.curselection()
    if choice:
      group = listbox.get(choice[0])
      cur_window.destroy()
      label.config(text=f"Вибрано групу {group}")

  cancel_button = tk.Button(bottom_frame, text="Відміна", padx=10, borderwidth=1, relief="raised", command=work2_window.destroy)
  cancel_button.grid(row=0,column=0, padx=5)
  yes_button = tk.Button(bottom_frame, text="Так", padx=10, borderwidth=1, relief="raised", command=lambda: on_select(group_list, work2_window, master_label))
  yes_button.grid(row=0, column=1, padx=5)

  GROUPS = ["ІМ-41", "ІМ-42", "ІМ-43", "ІМ-44", "ІП-41", "ІП-42", "ІП-43", "ІП-44",
             "ІП-45", "ІО-41", "ІО-42", "ІО-43", "ІО-44", "ІО-45", "ІО-46", "ІС-41",
               "ІС-42", "ІС-43", "ІС-44", "ІК-41", "ІК-42", "ІК-43", "ІК-44"]

  for group in GROUPS:
    group_list.insert("end", group)

  scrollbar.config(command=group_list.yview)
