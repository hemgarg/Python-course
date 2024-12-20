from datetime import date, time, datetime

#Calling the today
#Function of date class
today = date.today()
now = datetime.now()
print("Today's date is0", today)
print("\nCurrent date and time is", now)

print("\nDate components", today.year, today.month, today.day)