#Take input of a word
string = input("Please enter your own word")
#Take input of a character
char = input("Please enter your own character")
i = 0
count = 0
#Loop will to find the occurence of character
while(i < len(string)): 

    if (string[i] == char):
        count = count + 1
    i = i + 1

#Display result
print("The total number of time ", char, "Has occured = ", count)