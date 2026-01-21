class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [float("inf") for _ in range(len(s))]

        # left to right
        for i in range(len(s)):
            if s[i] == c:
                res[i] = 0
            elif i > 0:
                res[i] = res[i - 1] + 1

        # right to left
        for i in range(len(s) - 2, -1, -1):
            res[i] = min(
                res[i],
                res[i+1] + 1
            )
        
        return res

#T:O(n)
#S:O(1)
