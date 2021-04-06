import tkinter as tk
from tkinter import *

def ent(number):
   numone = total.get()
   total.delete(0, END)
   total.insert(0, numone + number )



def ent_clear():
    total.delete(0, END)



def ent_add():
    num1 = total.get()
    global initnum
    global operator
    operator = "+"
    initnum = int(num1)
    total.delete(0, END)


def ent_minus():
    num1 = total.get()
    global initnum
    global operator
    operator = "-"
    initnum = int(num1)
    total.delete(0, END)



def ent_times():
    num1 = total.get()
    global initnum
    global operator
    operator = "X"
    initnum = int(num1)
    total.delete(0, END)



def ent_divide():
    num1 = total.get()
    global initnum
    global operator
    operator = "/"
    initnum = int(num1)
    total.delete(0, END)



def ent_equals():
    num2 = total.get()
    total.delete(0, END)
    if operator == "+":
        total.insert(0, initnum + int(num2))

    if operator == "-":
        total.insert(0, initnum - int(num2))

    if operator == "X":
        total.insert(0, initnum * int(num2))

    if operator == "/":
        total.insert(0, initnum / int(num2))




form = tk.Tk()
form.title("Calculator GUI")
fullStringVar=tk.StringVar()

total=tk.Entry(form, font=('Verdana',18), width=15,borderwidth=10)
total.grid(columnspan=4, padx=10,pady=10)

button1 =tk.Button(form, text="1",padx=30,pady=20,command=lambda: ent("1"))
button2 =tk.Button(form, text="2",padx=30,pady=20,command=lambda: ent("2"))
button3 =tk.Button(form, text="3",padx=30,pady=20,command=lambda: ent("3"))
button4 =tk.Button(form, text="4",padx=30,pady=20,command=lambda: ent("4"))
button5 =tk.Button(form, text="5",padx=30,pady=20,command=lambda: ent("5"))
button6 =tk.Button(form, text="6",padx=30,pady=20,command=lambda: ent("6"))
button7 =tk.Button(form, text="7",padx=30,pady=20,command=lambda: ent("7"))
button8 =tk.Button(form, text="8",padx=30,pady=20,command=lambda: ent("8"))
button9 =tk.Button(form, text="9",padx=30,pady=20,command=lambda: ent("9"))
button0 =tk.Button(form, text="0",padx=30,pady=20,command=lambda: ent("0"))
button_plus =tk.Button(form, text="+",padx=30,pady=20,command=ent_add)
button_minus =tk.Button(form, text="-",padx=31,pady=20,command=ent_minus)
button_times =tk.Button(form, text="X",padx=30,pady=20,command=ent_times)
button_divide =tk.Button(form, text="/",padx=30,pady=20,command=ent_divide)
button_equals =tk.Button(form, text="=",padx=75,pady=20,command=ent_equals)
button_clear =tk.Button(form, text="Clr",padx=25,pady=20,command=ent_clear)

button1.grid(row=3,column=2)
button2.grid(row=3,column=1)
button3.grid(row=3,column=0)
button4.grid(row=2,column=2)
button5.grid(row=2,column=1)
button6.grid(row=2,column=0)
button7.grid(row=1,column=2)
button8.grid(row=1,column=1)
button9.grid(row=1,column=0)
button0.grid(row=4,column=1)
button_plus.grid(row=3,column=4)
button_minus.grid(row=2,column=4)
button_times.grid(row=1,column=4)
button_divide.grid(row=0,column=4)
button_equals.grid(row=4,column=2, columnspan=3)
button_clear.grid(row=4,column=0)

form.mainloop()