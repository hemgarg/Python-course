def get(x):
    binx = bin(x)[2:]
    binx2 = list(binx)
    bcount = 0
    ccount = 0
    for i in range(len(binx2)):
        if binx2[i] == "1":
            ccount += 1
        elif binx2[i] == "0" and ccount > bcount:
            bcount = ccount
            ccount = 0
    if ccount > bcount:
        bcount = ccount
        ccount = 0
    return bcount

num = int(input("Please enter an integer"))
print("The most amount of 1's consecutively in the binary represenative of your integer is",get(num))            