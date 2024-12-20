import math

H = int(input("Please enter the hypotenuse of the triangle"))
Opp = int(input("Please enter the opposite of the triangle"))
A = int(input("Please enter the Adjacent of the triangle"))

function = input("Please enter if you want to calculate the sine cos or tan")

if function == "sine":
    print("The sine of your triangle is " +str (math.sin(Opp / H)))
elif function == "cos":
    print("The cos of your triangle is " +str (math.cos(A / H)))

elif function == "tan":
    print("The targent of your triangle is " +str(math.tan(Opp / A)))
else:
    print("Wrong input")

