class Iostring:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = str(input("Please enter the string"))
    def print_string(self):
        print("Result is",self.str1.upper())

obj = Iostring()
obj.get_string()
obj.print_string()