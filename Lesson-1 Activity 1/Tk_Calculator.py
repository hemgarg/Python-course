from tkinter import *

Root = Tk()
Root.title("Calculator")
Root.geometry("300x400")

lbl = Label(text="Calculator", fg='white', bg="#Ff0000", height=2, width=100)

number1_entry = Entry()
number2_entry = Entry()

anstext = Text(height=1, width=20)

result = 0

def add():
    global result
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 + num2

def subtract():
    global result
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 - num2

def multiplication():
    global result
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 * num2

def division():
    global result
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    if num2 == 0:
        result = "Error (Divide by 0)"
    else:
        result = num1 / num2

def calculateans():
    anstext.delete(1.0, END)
    anstext.insert(END, str(result))

# Create a frame to hold the operation buttons
btn_frame = Frame(Root)

# Create buttons
Addbtn = Button(btn_frame, text="Add", command=add, height=1, bg="#1261A0", fg="white", width=8)
subtractbtn = Button(btn_frame, text="Subtract", command=subtract, height=1, bg="#1261A0", fg="white", width=8)
Multiplybtn = Button(btn_frame, text="Multiply", command=multiplication, height=1, bg="#1261A0", fg="white", width=8)
Dividebtn = Button(btn_frame, text="Divide", command=division, height=1, bg="#1261A0", fg="white", width=8)

Calculate = Button(text="Calculate", command=calculateans, height=1, bg="#1261A0", fg="white")

# Arrange widgets using grid layout
lbl.pack()
number1_entry.pack()
number2_entry.pack()
btn_frame.pack()  # Pack the frame (containing all buttons)

# Use grid inside the frame to align buttons in a single row
Addbtn.grid(row=0, column=0, padx=5, pady=5)
subtractbtn.grid(row=0, column=1, padx=5, pady=5)
Multiplybtn.grid(row=0, column=2, padx=5, pady=5)
Dividebtn.grid(row=0, column=3, padx=5, pady=5)

Calculate.pack()
anstext.pack()

Root.mainloop()
