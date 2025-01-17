class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructon called")

def obj_creation():
    print("Creating object")
    obj = Employee()
    print("Function end")
    return obj

print("Calling createobj function.....")
obj = obj_creation()
print("Program end")