numbers = input("Please enter the numbers separated by spaces: ").split()

numbers = [int(x) for x in numbers]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even)
print("Odd numbers:", odd)

#Start of other part

fruits = (["apple", "banana", "cherry", "kiwi", "mango"])
new_fruits_word1 = [fruits[0]]

new_fruits_char1 = [new_fruits_word1[0]]

new_fruits_char1 = str(new_fruits_word1[0])

new_fruits_char1 = new_fruits_char1.capitalize()

new_fruits_word1 = 'pple'

result = []

result.append(new_fruits_char1)

new_fruits_word2 = [fruits[1]]

new_fruits_char2 = [new_fruits_word2[0]]

new_fruits_char2 = str(new_fruits_word2[0])

new_fruits_char2 = new_fruits_char2.capitalize()

result.append(new_fruits_char2)

new_fruits_word3 = [fruits[2]]

new_fruits_char3 = [new_fruits_word3[0]]

new_fruits_char3 = str(new_fruits_word3[0])

new_fruits_char3 = new_fruits_char3.capitalize()

result.append(new_fruits_char3)


new_fruits_word4 = [fruits[3]]

new_fruits_char4 = [new_fruits_word4[0]]

new_fruits_char4 = str(new_fruits_word4[0])

new_fruits_char4 = new_fruits_char4.capitalize()

result.append(new_fruits_char4)


new_fruits_word5 = [fruits[4]]

new_fruits_char5 = [new_fruits_word5[0]]

new_fruits_char5 = str(new_fruits_word5[0])

new_fruits_char5 = new_fruits_char5.capitalize()

result.append(new_fruits_char5)

print(result)




