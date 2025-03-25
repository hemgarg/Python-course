from tkinter import * 

root = Tk()
root.geometry("400x400")
root.title("Password strength checker app")
root.configure(bg = "light blue")

Strength = Label(width = 10, bg = "white")

def Checkstrengthofpswrd():
    Pswrd = EnterPassword.get()
    Pswrd = list(Pswrd)
    Length = len(Pswrd)
    if Length <= 5:
        Strength.config(bg = "#ff422e")
    elif Length <= 8:
        Strength.config(bg = "#e97800")
    elif Length <= 12:
        Strength.config(bg = "#03cc00")
    elif Length > 13:
        Strength.config(bg = "#015400")

EnterPassword = Entry(width = 25, fg =  "black", background="white")
Checkstrength = Button(text = "Check strength", fg = "black", bg = "orange", command = Checkstrengthofpswrd)
enterpasswordtext = Text(width = 22,height = 1, fg = "black", background= "light blue", font = ("Arial", 10), relief=FLAT)
enterpasswordtext.insert(END,"Enter Password below me")
enterpasswordtext.config(state=DISABLED)
strengthtext = Text(width = 35, height = 1, fg = "black", background= "light blue", font = ("Arial", 10), relief=FLAT)
strengthtext.insert(END,"The strength of your password is -")
strengthtext.config(state = DISABLED)

EnterPassword.place(y = 100, x = 120)
enterpasswordtext.place( y = 70, x = 120)
strengthtext.place( y = 170, x = 200, anchor="center")
Strength.place(anchor="center", x = 200 , y = 200 )
Checkstrength.place( x = 200, anchor = "center", y = 230)

root.mainloop()

