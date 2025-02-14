class BMW:
    def __init__(self,max_speed,fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
class Ferrari:
    def __init__(self,maxspeed,fueltype):
        self.fueltype = fueltype
        self.maxspeed = maxspeed

bmwseed = BMW(150,"Petrol")
ferrariseed = Ferrari(200,"Diesel")

print("The fuel type of the BMW is \n",bmwseed.fuel_type,"\nAnd the max speed is \n",bmwseed.max_speed, "\n\n")
print("The fuel type of the BMW is \n",ferrariseed.fueltype,"\nAnd the max speed is \n",ferrariseed.maxspeed)
