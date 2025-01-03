Set1_input = input("Please enter set1 in all lowercase sepperated by commas")
Set2_input = input("Please enter set 2 in all lowercase seperated by commas")

Set1 = set(Set1_input.split(","))
Set2 = set(Set2_input.split(","))

Set3 = Set1.symmetric_difference(Set2)


print(Set3)