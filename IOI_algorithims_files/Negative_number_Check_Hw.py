def negative():
    try:
        n = int(input("Enter a number "))
    except ValueError:
        print("\nNot a number!\n")
        negative()
    if n < 0:
        print("\nNumber is negative\n")
        return
    else:
        print("\nNot negative\n")
        negative()

negative()