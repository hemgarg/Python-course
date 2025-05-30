def primeSeive():
    prime = [True for i in range(99+1)]
    currentnumber = 2 
    while (currentnumber * currentnumber <= 99):
        if (prime[currentnumber] == True):
            for i in range(currentnumber ** 2, 99 + 1, currentnumber):
                prime[i] = False
        currentnumber += 1

    prime[0] = False
    prime[1] = False
    for p in range(8,99+1):
        if prime[p]:
            print(p)

primeSeive()

