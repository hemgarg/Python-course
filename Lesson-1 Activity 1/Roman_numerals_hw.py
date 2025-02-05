try:
    integer = int(input("Please enter a number to convert to roman numerals: "))
except ValueError:
    print("That is not an integer! Please try again")
    exit()

romannumbers = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400, 
    "C": 100, "XC": 90, "L": 50, "XL": 40, 
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
}

result = ''

for numeral, value in romannumbers.items():
    while integer >= value:
        result += numeral
        integer -= value

if __name__ == "__main__":
    print(result)
