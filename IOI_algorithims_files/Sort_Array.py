a = [2, 0, 1, 2, 0, 2, 1, 1, 0, 2]
print(f"The array is {a} \n")

low = mid = 0
high = len(a) - 1

while mid <= high:
    if a[mid] == 0:
        a[low], a[mid] = a[mid], a[low]
        low += 1
        mid += 1
    elif a[mid] == 1:
        mid += 1
    else:
        a[mid], a[high] = a[high], a[mid]
        high -= 1

print("After Sorting", a)