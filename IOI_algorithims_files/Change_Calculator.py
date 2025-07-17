def count_ways_to_divide_money(amount, denominations):
    dp = [0] * (amount + 1)
    dp[0] = 1 # There's 1 way to make amount 0 (use nothing)

# For each coin, update the number of ways to make all values from coin to amount
    for coin in denominations:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


amount = int(input("Enter amount: "))
times = int(input("Please enter number of denominations"))
denominations = []

for i in range (times):
    x = int(input("Enter denomination"))
    denominations.append(x)
    

ways = count_ways_to_divide_money(amount, denominations)

print(f"There are {ways} ways to divide ₹{amount} using denominations {denominations}.")