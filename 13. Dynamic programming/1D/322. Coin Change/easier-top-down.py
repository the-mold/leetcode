class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {
            0: 0
        }

        def solve(amt):
            if amt in memo:
                return memo[amt]

            res = float("inf")
            for coin in coins:
                diff = amt - coin # find the diff between searched amount and current coin
                if diff < 0:
                    break
                res = min(res, 1 + solve(diff)) # find minimum of current amoutnt and 1 coin + number of coins needed to build the diff.
            
            memo[amt] = res
            return res
        
        res = solve(amount)
        if res < float("inf"):
            return res
        else:
            return -1

#T:(amount * number of coins)
#S:(amount), because of number of recursive function calls

# Testrun1 =====================
#[2] amount=3
# solve(3)
#   coin=2
#   diff=1
#   res=min(inf, 1 + solve(1)
          
# solve(1)
#   res = float("inf")
#   res=min(float("inf"), 1 + float("inf"))
#   return float("inf")

# back to solve(3):
#   res = float("inf")
#   res=min(float("inf"), 1 + float("inf"))
#   return float("inf")
  
  
# Testrun2 =====================
#[1,2,5] amount=11
# solve(11)
#   coin=1
#   diff=10
#   res=min(res, 1+solve(10))
  
# solve(10)
#   coin=1
#   diff=9
#   res=min(res, 1+solve(9))

# ...
# solve(2)
#   coin=1
#   diff=1
#   res=min(res, 1+solve(1))

# solve(1)
#   coin=1
#   diff=0
#   res=min(res, 1+solve(0))
#   return 1
  
# back to solve(2):
#   res=min(res, 1+1)
#   res = 2