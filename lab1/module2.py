import tkinter as tk
from tkinter import messagebox

def second_window(master, back_callback=None):
  work1_window2 = tk.Toplevel(master)
  work1_window2.geometry("400x200+500+250")
  work1_window2.title("Work 1 (second window)")
  work1_window2.resizable(False, False)

  def positive_click(window):
    window.destroy()
    messagebox.showinfo("Робота виконана!", "У нас усе вийшло!")

  bottom_frame = tk.Frame(work1_window2)
  bottom_frame.pack(side="bottom", pady=10)

  cancel_button = tk.Button(bottom_frame, text="Відміна", padx=10, borderwidth=1, relief="raised", command=work1_window2.destroy)
  cancel_button.grid(row=0, column=0, padx=5)
  back_button = tk.Button(bottom_frame, text="Назад", padx=10, borderwidth=1, relief="raised", command=lambda: back_callback(work1_window2) if back_callback else None)
  back_button.grid(row=0, column=1, padx=5)
  yes_button = tk.Button(bottom_frame, text="Так", padx=10, borderwidth=1, relief="raised", command=lambda: positive_click(work1_window2))
  yes_button.grid(row=0,column=2, padx=5)