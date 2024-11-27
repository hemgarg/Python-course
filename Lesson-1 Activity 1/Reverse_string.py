#Input the word or sentence
string = input("Please enter your Own string :")

string2 = ('')
#Loop for printing in reverse 
for i in string:
    string2 = i + string2

print("\nThe original string = " ,string)
print("\nThe reversed string = " ,string2)