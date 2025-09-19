import tkinter as tk

def first_window(master, next_callback=None):
  work1_window1 = tk.Toplevel(master)
  work1_window1.geometry("400x200+500+250")
  work1_window1.title("Work 1 (first window)")
  work1_window1.resizable(False, False)

  bottom_frame = tk.Frame(work1_window1)
  bottom_frame.pack(side="bottom", pady=10)

  cancel_button = tk.Button(bottom_frame, text="Відміна", padx=10, borderwidth=1, relief="raised", command=work1_window1.destroy)
  cancel_button.grid(row=0,column=0, padx=5)
  next_button = tk.Button(bottom_frame, text="Далі", padx=10, borderwidth=1, relief="raised", command=lambda: next_callback(work1_window1) if next_callback else None)
  next_button.grid(row=0, column=1, padx=5)
