#Take marks inputted from user
print("Enter Marks Obtained in 4 Subjects")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

#Calculation of precentage
sum = math+english+science+hindi
print ("Sum of math,english,science and hindi")
perc = (sum/400)*100

print (end="Percentage Mark =")
print (perc)