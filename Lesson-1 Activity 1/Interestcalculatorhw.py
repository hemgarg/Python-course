from tkinter import *

window = Tk()
window.title("Interest calculator")
window.geometry("600x400")

CIl = Label(width = 20,font = ("Arial", 12))
SIL = Label(width = 20,font = ("Arial", 12))

def calculate():
    P = float(PE.get())
    R = float(TE.get())
    T = float(RE.get())

    global SI
    SI = P * R * T / 100
    global CI
    CI = P * ((1 + R/100) ** T - 1)
    CIl.config(text = CI)
    SIL.config(text = SI)

Pr = Label(width = 11, font = ("Arial", 11), text =  "Enter principal")
Ti = Label(width = 15, font = ("Arial", 11), text =  "Enter Time in yrs")
Ra = Label(width = 14, font = ("Arial", 11), text =  "Enter Rate")

PE = Entry(width = 20)
TE = Entry(width = 20)
RE = Entry(width = 20)

Getinterest = Button(command = calculate, text = "Calculate interest", width = 30, height = 1)

CIT = Label(width = 20, font = ("Arial", 17), text =  "Compound interest:")

SIT = Label(width = 20, font = ("Arial", 17), text =  "Simple interest:")

Pr.place( x=50, y = 100)
Ti.place(x = 150, y= 100)
Ra.place(x = 275, y = 100)
Getinterest.place(y = 210, x = 300)

PE.place(x = 50,y= 150)
TE.place(x = 150,y= 150)
RE.place(x = 250,y= 150)

CIT.place(x = 150, y = 250)
SIT.place(x = 300,y = 250)
CIl.place(x = 200,y=350)
SIL.place(x = 400, y =350)

window.mainloop()