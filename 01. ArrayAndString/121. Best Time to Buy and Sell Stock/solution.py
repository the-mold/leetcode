def maxProfit(prices: list[int]) -> int:
  l = 0
  r = 1
  
  profit = 0
  while r < len(prices):
    if prices[l] < prices[r]:
      profit = max(profit, prices[r] - prices[l])
    else:
      l = r
    
    r += 1
  
  return profit

# T:O(n)
# S:O(1)