#Take input for the student that he can attend the exam or not
medical_cause = input("Did you have a medical cause Y or N: ")
#Take input of the attendance
attendance = int(input("Enter the attendance of the student: "))

#Checking the user input predicting output accordingly

if medical_cause == 'Y' : #Checking the conditon 1
    print ("You are allowed")
else:
    if attendance>=75:  #checking the condition 2
        print ("Allowed")
    else:  
        print ("not allowed")