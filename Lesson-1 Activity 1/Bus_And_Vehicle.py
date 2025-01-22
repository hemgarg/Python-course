class Vehicle:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

Busobject = Bus("Bus school voleo",50,100)
print("Name is {} \nSpeed is {} \nMileage is {}".format(Busobject.name, Busobject.speed, Busobject.mileage))
