def Max_Difference(b,s,b_size,s_size):
    min = s[0]
    max = b[0]
    for i in range(b_size-1):
        if b[i] > max:
            max == b[i]
    for i in range(s_size-1):
        if s[i] < min:
            min == s[i]

    return max-min

s = []
s_size = int(input("Enter the length of the 1st array: "))
for i in range(s_size):
    x = int(input("Enter number: "))
    s.append(x)

b = []
b_size = int(input("Enter the length of the 2nd array: "))
for i in range(b_size):
    x = int(input("Enter number: "))
    b.append(x)

print(f"The maximum difference of the greatest and smallest between the two arrays are: {Max_Difference(b,s,b_size,s_size)}")

