def maxProfit(prices: list[int]) -> int:
    min_price_to_buy_so_far = prices[0]
    largest_difference_between_buy_and_sell = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price_to_buy_so_far:
            min_price_to_buy_so_far = prices[i]
        else:
            largest_difference_between_buy_and_sell = max(largest_difference_between_buy_and_sell, prices[i] - min_price_to_buy_so_far)

    return largest_difference_between_buy_and_sell

#Intuition: keep track of lowest possible price to buy. Otherwise calculate how much you would earn on any given day.

#T: O(n)
#S: O(1)