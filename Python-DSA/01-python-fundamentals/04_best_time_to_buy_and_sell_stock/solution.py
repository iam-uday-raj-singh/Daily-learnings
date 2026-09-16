def best_time_to_buy_and_sell_stock(prices):
    
    if len(prices) == 0:
        return 0
    
    buy = prices[0]
    profit = 0
    
    for i in range(1,len(prices)):
        if prices[i]< buy:
            buy = prices[i]
        elif prices[i]- buy > profit:
            profit = prices[i]-buy
            
    return profit

if __name__== "__main__":
    prices = list(map(int, input("Enter stock seperated by spaces: ").split()))
    result = best_time_to_buy_and_sell_stock(prices)
    print("Maximum Profit: ", result)