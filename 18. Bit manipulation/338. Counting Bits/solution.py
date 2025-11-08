class Solution:
    def countOnes(self, n):
        ans = 0
        while n != 0:
            ans += 1
            n = n & (n-1)
        return ans

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countOnes(i))
        return res