print (" enter marks obitained in 5 subjects")
markOne = int(input("Maths"))
markTwo = int(input("English"))
markthree = int(input("Science"))
markfour = int(input("Hindi"))
markfive = int(input("SST"))

tot = markOne+markTwo+markthree+markfour+markfive
avg = tot/5

if avg >=91 and avg <=100:
    print ("Your grade is A1")
elif avg>=81 and avg<91:
    print ("Your grade is A2")
elif avg>=71 and avg<81:
    print ("Your grade is B1")
elif avg>=61 and avg<71:
    print ("Your grade is B2")
elif avg>=51 and avg<61:
    print ("Your grade is C1")
elif avg >=41 and avg<51:
    print ("Your grade is C2")
elif avg >= 33 and avg <51:
    print ("Your grade is D")
elif avg>= 21 and avg<33:
    print ("Your grade is E1")
elif avg>=0 and avg<21:
    print ("Your grade is E2")
else:
    print("Invalid Input!")
