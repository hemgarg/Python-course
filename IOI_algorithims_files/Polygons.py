class Polygon:
    def __init__(self,length,height,breadth):
        self.length = length
        self.height = height
        self.breadth = breadth
    def If3D(self):
        area = self.breadth * self.height * self.length
        print(F"The area of the Polygon is {area}")
    def if2D(self):
        area = self.height * self.length
        print(F"The area of the Polygon is {area}")
def therest():
    try:
        lent = int(input("Please Enter the length of the Polgyon "))
        heig = int(input("Please Enter the height of the polygon "))

        If2dornot = input("Please enter if 2d or not. If it's 2D enter 2D. If its 3D enter 3D. ")
        if If2dornot.lower() == "2d":
            obj = Polygon(lent,heig,1)
            obj.if2D()

        else:
            bread = int(input("Please enter the breadth of the polygon "))
            obj = Polygon(lent,heig,bread)
            obj.If3D()

    except ValueError:
        print("Please enter something an integer")
        therest()
therest()