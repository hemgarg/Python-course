actual_cost = float(input("Please Enter the Actual Product price:"))
sale_amount = float(input("Please Enter the Sales Amont:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print ("Total profit = {0}".format(amount))

else: 
    print ("No Profit!!!!!")