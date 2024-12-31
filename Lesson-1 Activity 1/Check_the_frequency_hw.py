test_dic = {"Codingal": 3, "is" : 2, "best" :2, "for" :2, 'Coding' :1}

print("The dicionary is ",str(test_dic))
char = int(input("Please enter the number you would like to check the frequency for"))

occ = 0 
for key in test_dic:
    if test_dic[key] == char:
        occ +=1

print("The amount of time the integer comes in the list is",occ)

