from tkinter import *
import random


root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#FF8400")
choice = ""
result_label = Label(root,bg = "#4C8ED9" ,fg = "black",width = 50,text = "Result comes here")

result_label.place(x = 50, y = 100)


def rock():
    global choice
    choice = "rock"


def paper():

    global choice
    choice = "paper"


def scissors():
    global choice
    choice = "scissors"
 

def choosewinner():

    cchoice = random.choice(["rock","paper","scissors"])


    if not choice:
        result_label.config(text = "Please choose rock, paper or scissors")
        return

    if cchoice == choice:
        result_label.config(text = "Its a draw!")

    elif choice == "rock":
        if cchoice == "paper":
            result_label.config(text="Sorry but you lost.")
        elif cchoice == "scissors":
            result_label.config(text = "Congratulations! You WIN.")


    elif choice == "paper":
        if cchoice == "rock":
            result_label.config(text = "Congratulations! You WIN.")
        elif cchoice == "scissors":
            result_label.config(text="Sorry but you lost.")


    elif choice == "scissors":
        if cchoice == "paper":
            result_label.config(text = "Congratulations! You WIN")
        elif cchoice == "rock":
            result_label.config(text="Sorry but you lost.")



rockbutton = Button(height = 1, width = 10, text = "ROCK", command=rock)
paperbutton = Button(height = 1, width = 10, text = "PAPER", command=paper)
scissorsbutton = Button(height = 1 , width = 10 , text= "SCISSORS", command = scissors)
winnerbtn = Button(height = 1, width = 25, text = "See who won",command = choosewinner)

rockbutton.place(x = 25, y = 200)
scissorsbutton.place(y = 200, x = 300)
paperbutton.place(y = 200, x = 165)
winnerbtn.place(x = 100, y = 150)

root.mainloop()