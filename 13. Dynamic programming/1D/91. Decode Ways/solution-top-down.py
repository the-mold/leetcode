#Intuition: you are checking in how many ways you can reach the last char, if you move by +1 and +2 steps. The idea is to invalidate some certain decoding attempt in the child function and return 0 if it does not work. Otherwise return 1 to signalize that you reached the end of the string.
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {
            # base case: if I reach the end of the string it is 1
            len(s): 1
        }

        def solve(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0

            # --- Recursive Step: Explore the choices ---

            # Choice 1: Decode a single digit (s[i]).
            # This is always possible if s[i] is not '0'.
            # The number of ways is the result of decoding the rest of the string.
            res = solve(i+1)
            
            # Choice 2: Decode two digits (s[i] and s[i+1]).
            # This is only possible if we're not at the end of the string AND
            # the two-digit number is between 10 and 26.
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += solve(i+2)

            memo[i] = res
            return res
        
        # how many ways to decode the string if i stat at index 0
        return solve(0)