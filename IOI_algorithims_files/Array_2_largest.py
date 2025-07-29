def print2largest(a,a_size):

    largest = secondlargest = -2147483648

    for i in range(a_size):
        if (a[i] > largest):
            secondlargest = largest
            largest = a[i]
        
        elif (a[i] > secondlargest and a[i] != largest):
            secondlargest = a[i]
    print("second largest")

a = [1,2,3,4,5,6,7,8,9]
a_size = len(a)
print2largest(a,a_size)