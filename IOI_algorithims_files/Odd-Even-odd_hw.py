def odd_even(a, a_size):
    if a_size == 0:
        return 0
    

    max_sum = a[0]
    current_sum = a[0]


    for i in range(1, a_size):

        if (a[i] % 2 == 0 and a[i-1] % 2 != 0) or (a[i] % 2 != 0 and a[i-1] % 2 == 0):

            current_sum += a[i]
        else:

            current_sum = a[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return f"Biggest subarray is equal to {max_sum}"

a = []
a_size = int(input("Enter size of array: "))
for i in range(a_size):
    x = int(input("Enter the number: "))
    a.append(x)

print(odd_even(a, a_size))