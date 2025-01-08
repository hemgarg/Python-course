s1 = {1,3,5}
s2 = {2,4,6}
result = list(zip(s1, s2))
print(result)

list1 = [10, 20, 30, 40]
list2 = [100 , 200 , 300, 400]
for x,y in zip(list1, list2[::-1]):
    print(x, y)


stocks = ["Reliance","infosys" , "tcs"]
prices = [2175, 1127, 2750]
new_dict = {stocks: prices for stocks, prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))