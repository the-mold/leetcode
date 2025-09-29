class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num**2)

        return sorted(res)

#T:O(n log(n))
#S:O(n)