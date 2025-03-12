from tkinter import *

root = Tk()
root.title("Inches to cm calculator")
root.geometry("250x350")
root.configure(bg="#E59947")

# Greeting Frame and Label
greetframe = Frame(master=root, relief=RIDGE, borderwidth=5, height=50, width=200, bg="#4793E5")
greetframe.place(x=30, y=20)

greettext = Label(master=root, text="Inches to Centimeter Converter", font=("Calibri", 10), bg="#4793E5")
greettext.place(x=40, y=35)

# Entry Section (Side by Side)
inchtext = Label(master=root, text="Enter Inches", font=("Calibri", 15), bg="#E59947")
inchtext.place(x=30, y=80)  # Left side

inchentry = Entry(master=root, width=10, bg="#999898")
inchentry.place(x=150, y=85)  # Right side, aligned

# Answer Section (Side by Side, Below Entry)
cmtext = Label(root, text="The ans is -", font=("Calibri", 15), bg="#E59947")
cmtext.place(x=30, y=140)  # Left side

cmtextans = Label(root, text="0", font=("Calibri", 15), bg="#999898", width=5)
cmtextans.place(x=150, y=140)  # Right side, aligned

# Error Message (Initially Hidden)
errortext = Label(master=root, text="Sorry but that is not an integer!", font=("Calibri", 12), fg="red", bg="#E59947")
errortext.place(x=30, y=280)
errortext.place_forget()  # Hide initially

def calculation():
    try:
        errortext.place_forget()  # Hide error if previously shown
        inchentrynum = int(inchentry.get())  # Convert input to integer
        anscm = inchentrynum * 2.54  # Calculate cm
        cmtextans.config(text=str(anscm))  # Update label with the answer
    except ValueError:
        errortext.place(x=30, y=280)  # Show error message

# Calculate Button
calculatebtn = Button(text="Calculate", command=calculation, height=1, bg="#999898", width=7)
calculatebtn.place(x=125, y=220)

root.mainloop()
