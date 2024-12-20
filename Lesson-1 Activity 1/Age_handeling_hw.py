taking_age = True
while taking_age:
    try:
        age = int(input("Please enter an age"))
        if age % 2 > 0:
            print("This is an odd number age")
            break
        else:
            print("This is an even number age")
            break
    except:
        if ValueError:
            print("This is a wrong input! Please try again")

    