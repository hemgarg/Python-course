class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def info(self):
        print(f"Hello! I am {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def info(self):
        print(f"Hello! I am {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")

dog1 = Cat("Dodo",2.5)
cat1 = Dog("Tyson",8)

for i in dog1,cat1:
    i.info()
    i.make_sound()