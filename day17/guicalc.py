import tkinter as tk
from tkinter import ttk

def my_btn_handler():
    num_1 = text_field1.get()
    num_2 = text_field2.get()
    total_sum = int(num_1) + int(num_2)
    result_label.config(text="Result=" + str(total_sum))

window = tk.Tk()
window.title("First Program")
window.geometry("800x800")
window.minsize(width=400, height=800)

# Text fields
text_field1 = ttk.Entry(master=window)
text_field1.pack(pady=10)

text_field2 = ttk.Entry(master=window)
text_field2.pack(pady=10)

# Button
my_btn = ttk.Button(master=window, text="Add", command=my_btn_handler)
my_btn.pack(pady=10)

# Result Label
result_label = ttk.Label(master=window, text="Result=", font=("Arial", 40))
result_label.pack(pady=10)

window.mainloop()
