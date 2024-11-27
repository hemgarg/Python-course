#Take Input of number of units consumed from the user
units=int(input("Please enter Number of Units you have Consumed :"))

#Check condinitions of units consumed
# Then calculate amount and surcharge accordingly
# surcharge its tax value

# check for units less than 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

#Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

#check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 152.50 + ((units - 100) * 5.26)
    surcharge = 45
    
#Check for all the cases other than mentioned
#When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

#Calculate and Display the total electricity bill
#Total amount = amount + surcharge


Total = amount + surcharge
print ("\nElectricity Bill = %.2f"  %Total)