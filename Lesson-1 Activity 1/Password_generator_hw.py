import random
import array as arr

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_case_letters = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K' , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


random_password =[]
True_or_False = ["True", "False"]

for i in range (7):
    upper_or_not = random.choice(True_or_False)
    if upper_or_not == "True":
        randomletter = random.choice(upper_case_letters)
        random_password.append(randomletter)
    else:
        randomletter = random.choice(letters)
        random_password.append(randomletter)

for j in range(5):
    random_number = random.choice(numbers)
    random_password.append(random_number)


print("The password is --",random_password[1],random_password[2],random_password[3],random_password[4],random_password[5],random_password[6],random_password[7],random_password[8],random_password[9],random_password[10],random_password[11])