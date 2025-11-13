class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) == k:
                    count += 1

        return count 

# T:O(n**3)
# S:O(1)
