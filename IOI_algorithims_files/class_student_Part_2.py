class student:
    grade = 10 
    name = "Penguin"

    def introduction(self):
        print("Hi i am a student")
    def details(self):
        print(f"My name is -{self.name}")
        print(f"I study in Grade,{self.grade}")

ob = student()

ob.introduction()
ob.details()