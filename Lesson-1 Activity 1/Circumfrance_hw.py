def diameter(D, E):
    return D * E
def radius(D, E):
    return D * (E * 2)

#Take input
print("Choose what you know about the circle")
print("a. Radius")
print("b. Diameter")

choice = input("Please now enter the choice (a or b):")

if choice == "a":
    R = int(input("Now please enter the radius"))
    D = R * 2
    C = 3.141592653589793 * D
    print("So the circumfrance of the circle is",C)

elif choice == "b":
    D = int(input("Please now enter the diameter"))
    C = 3.141592653589793 * D
    print("So the circumfrance of the circle is",C)

else:
    print("Invalid input!")