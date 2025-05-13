class Computer:

    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling price {}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice = price
    
C = Computer()
C.sell()

C.__maxprice = 1000
C.sell()

C.setMaxPrice(1000)
C.sell()