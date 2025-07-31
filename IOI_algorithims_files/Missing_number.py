def Missingnumber(a,a_size):
    i = 0
    x = 1
    for i in range(a_size - 1):
        if x == a_size:
            return "none"
        if a[i] != x:
            return x
        else:
            i += 1
            x += 1
    
num = int(input("Please enter the size of the array: "))
a = []
for x in range(num):
    r = int(input("Enter number: "))
    a.append(r)
print(f"Missing number from the array is {Missingnumber(a,len(a))}")