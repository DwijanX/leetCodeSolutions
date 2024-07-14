

def maxProfit( prices, fee):
    profit=0
    alreadyBoughtPrice=prices[0]
    for price in prices:
        profit=max(profit,price-alreadyBoughtPrice-fee)
        alreadyBoughtPrice=min(alreadyBoughtPrice,price-profit)
    return profit

print(maxProfit([1,3,2,8,4,9],2)) #8