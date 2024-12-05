#Take input
print ("Half Pyramid Pattern of stars (*):")
n = int(input("Enter the number of rows:"))
#Outer loop to handle number of rows
for i in range(n):
    #Inner loop to handle number of columns
        for j in range(i+1):
            #Display result
                print("* ", end="")
        print()