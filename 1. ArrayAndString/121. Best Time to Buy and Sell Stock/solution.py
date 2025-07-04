def maxProfit(prices: list[int]) -> int:
    buy_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        else:
            profit = max(profit, prices[i] - buy_price)

    return profit

#Intuition: keep track of lowest buy_price OR possibility to sell on every given day.

#T: O(n)
#S: O(1)