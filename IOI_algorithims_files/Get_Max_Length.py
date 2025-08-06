def getMaxLength_a(a,a_size):
    counter = 0
    max_ones = 0
    for i in range(0,a_size):
        if(a[i] == 0):
            counter = 0
        else:
            counter += 1
            max_ones = max(max_ones,counter)
    return max_ones

a = [1,1,0,0,1,0,1,0,1,1,1,1]
a_size = len(a)
print("Max 1's : ",getMaxLength_a(a,a_size))