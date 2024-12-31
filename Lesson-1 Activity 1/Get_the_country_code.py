SPCMcountry_code = {'India': '0091',
                    "Australia" : '0025',
                    "Nepal": '00977'}

print("Country code for india - ")
print(SPCMcountry_code.get("India", ' NotFound'))

print("Country code for Japan-")
print(SPCMcountry_code.get("Japan", "Not found"))