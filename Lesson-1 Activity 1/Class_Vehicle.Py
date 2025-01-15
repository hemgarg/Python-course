class Vehicle:

    def __init__(self,max_speed, mileage):
        
        self.max_speed = max_speed
        self.mileage = mileage

model = Vehicle(240, 18)


print("The max speed is",model.max_speed)

print("The mileage is",model.mileage)
        