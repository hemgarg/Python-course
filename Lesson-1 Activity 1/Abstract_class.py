from abc import ABC

class Abstract(ABC):
    def print(self,x):
        print("The input is",x)
    def task(self): 
        print("We are in an abstract class ")
    
class test_class(Abstract):
    def task(self):
        print("We are inside test class")

testobject = test_class()
testobject.task()
testobject.print(100)