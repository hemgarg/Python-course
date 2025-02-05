class GetReverseString:
    def __init__(self, str1):
        self.str1 = str1
        self.str2 = ""
    
    def Reverse(self):
        # Reverse the string using slicing
        self.str2 = self.str1[::-1]
    
    def display(self):
        print("Reversed str is --", self.str2)


temp = input("Please enter the thing to be reversed: ")
userinput = GetReverseString(temp)
userinput.Reverse()
userinput.display()



            
            
        
