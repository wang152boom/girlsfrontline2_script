import tkinter as tk  # gui界面函数
from tkinter import messagebox


def main_gui():
    root = tk.Tk()
    root.title('主界面')
    b1 = tk.Button(root)
    b1["text"] = "click"
    b1.pack()
    b1.bind("<Button-1>", test)
    root.mainloop()


def test(e):
    messagebox.showinfo("name", "success click")
