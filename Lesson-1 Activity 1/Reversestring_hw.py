class GetReverseString:
    def __init__(self,str1):
        self.str1 = str1
        self.str2 = []
    def Reverse(self,str1):
        self.str1 = list(str1)
        x = len(self.str1)
        print(x)
        str2 = []
        for i in range (x):
            s = len(str1) - 1
            print(s)
            str2.append(s)
            s -= 1
    def display(str2):
        print("Reversed str is --",str2)


temp = input("Please enter the thing to be reversed")
userinput = GetReverseString(temp)

userinput.Reverse(userinput.str1)
userinput.display()


            
            
        
