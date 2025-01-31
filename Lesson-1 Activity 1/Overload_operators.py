class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a > other.a:
            return "ob1 is less then ob2"
    def __eq__(self,other):
        if self.a == other.a:
            return "Both are equal"
        elif self.a > other.a:
            return "ob1 is greater then ob2"
        elif self.a < other.a:
            return "ob2 is greater than ob1"
        
obj1 = A(4)
obj2 = A(3)

print("Passed values",obj1.a, obj2.a)
print(obj1 < obj2)

obj3 = A(4)
obj4 = A(4)

print("Passed values",obj3.a,obj4.a)
print(obj3 == obj4)