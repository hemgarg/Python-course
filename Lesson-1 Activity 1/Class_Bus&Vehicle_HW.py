class Vehicle():
    def __init__(self,total_cost):
        self.total_cost = total_cost

    def display(self):
        print("The total cost is --> ₹",self.total_cost)

class Bus(Vehicle):
    def __init__(total_cost):
        super().__init__(total_cost)

objBus = Vehicle(344)
objBus.display()
