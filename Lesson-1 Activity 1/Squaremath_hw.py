input1 = int(input("Please enter the lower number: "))
input2 = int(input("Please enter the higher number: "))
if input1 > input2:
    print("Sorry, but you provided numbers in the wrong order. Swapping them.")
    input1, input2 = input2, input1 

print("The numbers in the list are:")
for X in range(input1, input2 + 1):
    print(X)

print("The square of all of these numbers are:")
for X in range(input1, input2 + 1):
    sqr = X * X 
    print(sqr)