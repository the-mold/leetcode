class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        global_max = 1
        curr_max = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_max += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr_max = 1
            global_max = max(global_max, curr_max)
        
        return global_max

# T:O(nlogn)
# S:O(n)