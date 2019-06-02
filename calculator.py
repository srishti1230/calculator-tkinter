import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

heading_label_1=tk.Label(mainWindow,text="Enter first number",padx=(20),pady=(10))
heading_label_1.pack()

no_1=tk.Entry(mainWindow)
no_1.pack()

heading_label_2=tk.Label(mainWindow,text="Enter second number",padx=(20),pady=(10))
heading_label_2.pack()

no_2=tk.Entry(mainWindow)
no_2.pack()

heading_label_3=tk.Label(mainWindow,text="operation")
heading_label_3.pack()


def add():
    try:
        f=int(no_1.get())
        s=int(no_2.get())
        a=f+s
        print(a)
        result_label.config(text="sum:" + str(a))
    except ValueError:
        result_label.config(text='you can only enter int value')
def sub():
    try:
        f=int(no_1.get())
        s=int(no_2.get())
        b=f-s
        print(b)
        result_label.config(text="subtraction:"+str(b))
    except ValueError:
        result_label.config(text="you can enter only integer value")

def mul():
    try:
        f=int(no_1.get())
        s=int(no_2.get())
        c=f*s
        print(c)
        result_label.config(text="multiplication:" + str(c))
    except ValueError:
        result_label.config(text="you can enter only integer value")


def div():
    try:
        f=int(no_1.get())
        s=int(no_2.get())
        if (s != 0):
            d=f/s
            print(d)
            result_label.config(text="division:" + str(d))
        else:
            messagebox.showinfo("Error", "divisor can't be zero")
    except ValueError:
        result_label.config(text="you can enter only integer value")

button_1=tk.Button(mainWindow,text="+",command=lambda:add(),padx=(20),pady=(10))
button_1.pack()

button_2=tk.Button(mainWindow,text="-",command=lambda:sub(),padx=(20),pady=(10))## lambda removes direct calling of function else the the function would be called automatically
button_2.pack()

button_3=tk.Button(mainWindow,text="*",command=lambda:mul(),padx=(20),pady=(10))
button_3.pack()

button_4=tk.Button(mainWindow,text="/",command=lambda:div(),padx=(20),pady=(10))
button_4.pack()

heading_label_4=tk.Label(mainWindow,text="Result",padx=(20),pady=(10))
heading_label_4.pack()

result_label=tk.Label(mainWindow)
result_label.pack()
mainWindow.mainloop()
