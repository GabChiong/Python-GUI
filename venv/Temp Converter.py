import tkinter as tk
from tkinter import *

def ent_calculate():
    total1.delete(0, END)
    temp = total.get()
    degree = int(temp[:-1])
    Dat1 = temp [-1]


    if Dat1.upper() == "C":
        final = int(round((9 * degree) / 5 + 32))
        Dat2 = "F"
    elif Dat1.upper() == "F":
        final = int(round((degree - 32) * 5 / 9))
        Dat2 = "C"
    else:
        total1.insert(0, ERROR)
        total.delete(0, END)
    finalanswer = final,Dat2
    total1.insert(0, finalanswer)
    total1.config(state=DISABLED)



form = tk.Tk()
form.title("Automatic Temp. Calculator")
fullStringVar=tk.StringVar()

tempguide=tk.Label(form, font=('Verdana',10),text = "Apply temperature symbol (C,F) \n at the end of the measurement")
tempguide.grid(row=0,column=0,columnspan=3,padx=20,pady=10)

temp=tk.Label(form, font=('Verdana',10,'bold'),text = "ENTER HERE")
temp.grid(row=1,column=0,columnspan=1,padx=2,pady=2)

result1=tk.Label(form, font=('Verdana',10,'bold'),text = "RESULT")
result1.grid(row=1,column=1,columnspan=2,padx=2,pady=2)

total=tk.Entry(form, width=5,borderwidth=10,font=('Verdana',20,'bold'))
total.grid(row=2,column= 0, columnspan=1, padx=10,pady=10)

total1=tk.Entry(form, width=5,borderwidth=10,font=('Verdana',20,'bold'))
total1.grid(row=2,column=1,columnspan=2, padx=10,pady=10)

result =tk.Button(form, text="Calculate",font=('Verdana',10,'bold'),padx=30,width=20,pady=5,command=ent_calculate)
result.grid(row=3,columnspan=3)

form.mainloop()