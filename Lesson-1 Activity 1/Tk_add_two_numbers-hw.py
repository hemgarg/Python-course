from tkinter import *

root = Tk()
root.title("Multiplication program")
root.geometry("500x400")


lbl = Label(text ="Multiplication Program!", fg = 'white', bg = "#Ff0000", height = 1, width = 100)

onetext = Label(text = "Enter number 1")
twotext = Label(text = "Enter number 2")

def calculateans():
    result.delete('1.0',END)
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    global resultnum
    resultnum = num1*num2
    result.insert(END,resultnum)

calculatebtn = Button(text="Calculate", command = calculateans, height=1, bg = "#1261A0", fg="white")

number1_entry = Entry()
number2_entry = Entry()
result=Text(height = 1)



lbl.pack()
onetext.pack()
number1_entry.pack()
twotext.pack()
number2_entry.pack()
calculatebtn.pack()
result.pack()


root.mainloop()