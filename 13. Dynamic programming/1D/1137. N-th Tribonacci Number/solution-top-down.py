class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def solve(k):
            if k == 0:
                return 0
            if k == 1 or k ==2:
                return 1
            
            if k in cache:
                return cache[k]

            res = solve(k-1) + solve(k-2) + solve(k-3)
            cache[k] = res

            return res

        return solve(n)