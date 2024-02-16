import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("800x800")
window.minsize(width=400,height=400)
window.title("THIS IS MY FIRST GUI BASED PROGRAM")
#text field
my_textfield=ttk.Entry(master=window)
my_textfield.place(x=100,y=100)
#button declare

def button_handler():
    text_field_val=my_textfield.get()
    print (text_field_val)
#button
button=ttk.Button(master=window,text="hit me",command=button_handler)
button.place(x=250,y=100)  












window.mainloop()

