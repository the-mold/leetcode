class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        seen = [False for _ in range(n+1)]

        # check what lowest nums are in seen
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        
        for idx in range(1, n+1):
            if seen[idx] == False:
                return idx
        
        return n+1

# T:O(n)
# S:O(n)