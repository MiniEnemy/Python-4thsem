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
no1 = ttk.Label(master=window, text="enter ur number=", font=("Arial", 10))
no1.grid(row=0,column=0,pady=10)
text_field1 = ttk.Entry(master=window)
text_field1.grid(row=0,column=4,pady=10)
no2 = ttk.Label(master=window, text="enter ur number=", font=("Arial", 10))
no2.grid(row=1,column=0,pady=10)
text_field2 = ttk.Entry(master=window)
text_field2.grid(row=1,column=4,pady=10)

# Button
my_btn = ttk.Button(master=window, text="Add", command=my_btn_handler)
my_btn.grid(row=3,column=3,pady=0,sticky="w")

# Result Label
result_label = ttk.Label(master=window,  font=("Arial", 40))
result_label.grid(row=3,column=0,pady=0,columnspan=2)

window.mainloop()
