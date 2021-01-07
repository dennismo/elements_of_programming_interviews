# 5.7
def buy_stock_twice(stock_price):
    DP = [ 0 for _ in range(len(stock_price))]
    min = float("inf")
    for i, price in enumerate(stock_price):
        if price < min:
            min = price
        DP[i] = max(0, price - min)
    
    for i, price in enumerate(reversed(stock_price)):
        index = len(stock_price) - i - 1
        DP[i] += 

