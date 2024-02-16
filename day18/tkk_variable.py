import tkinter as tk
from tkinter import ttk

Window=tk.Tk()
Window.title("DEMO")
Window.geometry("400x800")

my_variable=tk.StringVar()

another_var=tk.IntVar()
another_var_1=tk.BooleanVar()

entry=ttk.Entry(textvariable=my_variable)
entry.pack(pady=10)

entry_label=ttk.Label(textvariable=my_variable)
entry_label.pack(pady=10)
Window.mainloop()