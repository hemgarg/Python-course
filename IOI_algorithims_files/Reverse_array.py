arro = []
num = int(input("Enter number of elements in the array: "))
for _ in range(num):
    x = input("Enter element")
    arro.append(x)
arrn = arro[::-1]
print(f"Reversed of {arro} is {arrn}")