pi = 3.141592653589793238462643383279502884197169399375105820974944

class Circle:
    def area(self,radius):
        area = pi * radius ** 2
        print(f"The area of the circle is ~ {area}")
    def perimeter(self,radius):
        perimetre = 2 * pi * radius
        print(f"The perimeter also known as circumference of the circle is ~ {perimetre}")

radius = ''

while True:
    try:
        radius = int(input("Please enter the radius of the circle"))
        break
    except ValueError:
        print("Sorry but thats not a valid value!")

obj = Circle()
obj.area(radius)
obj.perimeter(radius)
