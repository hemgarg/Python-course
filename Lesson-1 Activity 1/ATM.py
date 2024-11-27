Amount = int(input("Please enter amount for withdraw:"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
note_4 = (((Amount%100%10//1)))


print ("notes of 100 rupee",note_1)
print ("notes of 50 ruppe", note_2)
print ("notes of 10 ruppe", note_3)
print ("notes of 1 ruppe", note_4)