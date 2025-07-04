def recursivefunction1(n):
    if(n==1 or n==0):
        return 1
    return n*recursivefunction1(n-1) 

def recursivefunction2(n2):
    if n2 == 0: return
    print(n2)
    recursivefunction2(n2-1)


print("The Time complexity of recursive function1 (Prints Factorial is) O(N) (Linear time)")
print("The Time complexity of recursive function2 (Prints numbers 1-10 is) O(n\u00B2) (Quadtric time)")