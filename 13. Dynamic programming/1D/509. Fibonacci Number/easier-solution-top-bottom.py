class Solution:
    def fib(self, n: int) -> int:

        cache = {}
        
        def solve(n: int):
            if n == 0:
                return 0
            if n == 1:
                return 1

            if n in cache:
                return cache[n]
            
            res = solve(n-1) + solve(n-2)
            cache[n] = res

            return res
        
        return solve(n)

# Time Complexity: O(n)
# Why not O(2^n)? Without memoization, the time complexity would be exponential because you would re-compute the same Fibonacci numbers many times.
# How Memoization Helps: With the cache, each Fibonacci number from 2 to n is computed exactly once.
# When solve(k) is called for the first time, it does O(1) work (addition) and then makes two recursive calls.
# Every subsequent time solve(k) is called, it's an O(1) lookup from the cache.
# Since you compute each value from fib(2) to fib(n) only once, the total number of computations is proportional to n.
# Therefore, the time complexity is O(n).
# Space Complexity: O(n)
# There are two components to the space complexity:

# The Cache (cache):
# The cache dictionary will store the result for each number from 2 up to n.
# This requires space for n-1 key-value pairs.
# Space required for the cache is O(n).
# The Recursion Stack:
# The recursive calls create a call stack. The maximum depth of this stack will be n. For example, to compute solve(n), you will have solve(n-1), solve(n-2), ..., solve(1) on the stack at one point.
# The space required for the recursion stack is O(n).
# Combining these, the total space complexity is O(n) + O(n), which simplifies to O(n).




# Call sequence for fib(4)
# 1. solve(4)
#   4 not in cache 
#   res = solve(3) + solve(2)
  
#   2. solve(3)
#      3 not in cache 
#      res = solve(2) + solve(1)
     
#   3. solve(2)
#      2 not in cache 
#      res = solve(1) + solve(0)
#      save result for 2 in cache
     
#   4. solve(1)
#      1 is basecase, return 1
  
#   5. solve(0)
#      0 is basecase, return 0
     
#   6. Back to solve(3)
#     res = 1 + solve(1)
    
#   7. solve(1)
#      1 is basecase, return 1
  
#   8. 6. Back to solve(3)
#      res = 1 + 1
#      save in cache result for 3
     
#   9. back to solve(4)
#      res = 2 + solve(2) 
    
#   10. solve(2) 
#       get result from cache for 2
      
#   11. back to solve(4)
#       res = 2 + solve(1)
#       save result in cache for 4 