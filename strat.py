print("Enter odds in descending order")

odds = []
prices = []

for i in range(0, 3):
    odds.append(float(input("Enter Odd: \n")))
    prices.append(0.00)

prices[0] = float(input("What is the minimum amount of money you can bet? \n"))
prices[1] = (odds[0] / odds[1]) * prices[0]
prices[2] = (odds[0] / odds[2]) * prices[0]
#price_three_check = (odds[1] / odds[2]) * prices[1]

total_price = float(prices[0] + prices[1] + prices[2])
total_profit = float(prices[0] * odds[0])

print("Total price of bet = " + str(total_price))
print("Total return from bet = " + str(total_profit))
print("Actual profit from bet = " + str((total_profit - total_price)))
for i in range(0, 3):
    print("Bet " + str(prices[i]) + " on odd " + str(odds[i]))