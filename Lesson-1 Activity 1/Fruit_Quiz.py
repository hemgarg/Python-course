import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple': 'red',
                       'orange': 'orange',
                       'bannana': "yellow"}
    def quiz(self):
        while True:
            fruit,colour = random.choice(list(self.fruits.items()))

            print("What is the colour of {}".format(fruit))
            useranswer = input()
            if (useranswer.lower() == colour):
                print("Correct answer")
            else:
                print("Wrong answer!")
            option = int(input("Enter 0 if you want to play a gain otherwise enter 1"))
            if (option):
                break
print("Welcome to the fruit quiz")
fq = FruitQuiz()
fq.quiz()