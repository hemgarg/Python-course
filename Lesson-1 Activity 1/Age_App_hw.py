from tkinter import *
import datetime

# Initialize Tkinter Window
root = Tk()
root.geometry("350x400")
root.title("Age Calculator")

# Labels
Welcometxt = Label(text="Hello! This is an app to check your age", bg="#ADD8E6", height=1, width=40)
date = Label(text="Enter Date", bg="#ADD8E6", height=1, width=10)
month = Label(text="Enter Month", bg="#ADD8E6", height=1, width=10)
year = Label(text="Enter Year", bg="#ADD8E6", height=1, width=10)

# Text Inputs
datetxt = Text(bg="white", fg="black", height=1, width=25)
monthtxt = Text(bg="white", fg="black", height=1, width=25)
yeartxt = Text(bg="white", fg="black", height=1, width=25)
anstext = Text(bg="white", fg="black", height=3, width=35)

# Function to Calculate Age
def calculate():
    anstext.delete("1.0", END)  # Clear previous text

    try:
        datetext = int(datetxt.get("1.0", "end-1c").strip())
        monthtext = monthtxt.get("1.0", "end-1c").strip().lower()
        yeartext = int(yeartxt.get("1.0", "end-1c").strip())
    except ValueError:
        anstext.insert(END, "Invalid input! Please enter numbers.")
        return

    # Month conversion dictionary
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }
    monthnum = month_map.get(monthtext, None)
    
    if monthnum is None:
        anstext.insert(END, "Invalid month name!")
        return

    today = datetime.date.today()
    todaydate, todaymonth, todayyear = today.day, today.month, today.year

    # Calculate age
    ansyear = todayyear - yeartext
    ansmonth = todaymonth - monthnum
    ansdate = todaydate - datetext

    # Handle negative date (borrow days from the previous month)
    if ansdate < 0:
        prev_month = todaymonth - 1 if todaymonth > 1 else 12
        prev_year = todayyear if todaymonth > 1 else todayyear - 1  # Handle year change
        
        # Get days in the previous month
        month_days = {
            1: 31, 2: (29 if prev_year % 4 == 0 and (prev_year % 100 != 0 or prev_year % 400 == 0) else 28),
            3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        ansdate += month_days[prev_month]  # Borrow days
        ansmonth -= 1  # Reduce month count since we borrowed days

    # Handle negative month
    if ansmonth < 0:
        ansyear -= 1
        ansmonth += 12

    # **💡 FINAL FIX HERE!**
    if todaydate < datetext:
        ansmonth += 1

    anstext.insert(END, f"You are {ansyear} Years old, {ansmonth} Months old, and {ansdate} Days old")

# Button
calculatebtn = Button(text="Calculate Age", height=1, width=12, bg="#1261A0", fg="white", command=calculate)

# Positioning widgets
Welcometxt.place(x=5, y=10)
date.place(x=10, y=60)
month.place(x=10, y=110)
year.place(x=10, y=160)
datetxt.place(x=90, y=60)
monthtxt.place(x=90, y=110)
yeartxt.place(x=90, y=160)
anstext.place(y=250, x=10)
calculatebtn.place(y=200, x=10)

root.mainloop()
