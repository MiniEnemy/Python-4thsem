from tkinter import *

def button_click(event):
    text = event.widget.cget("text")
    if text == "=" and expression.get() != "":
        try:
            result = eval(expression.get())
            expression.set(result)
        except Exception as e:
            expression.set("Error")
    elif text == "C":
        expression.set("")
    else:
        expression.set(expression.get() + text)

root = Tk()
root.title("Simple Calculator")

expression = StringVar()
expression.set("")

entry = Entry(root, textvariable=expression, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    btn = Button(root, text=button, font=("Arial", 20), width=4, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()


