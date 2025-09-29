class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1

        max_sum = -1
        while l < r:
            local_sum = nums[l] + nums[r]
            if local_sum < k:
                max_sum = max(max_sum, local_sum)
                l += 1
            else:
                r -= 1

        return max_sum

#T:O(n log n) , becasue of sorting
#S:O(n log n) , becasue of sorting
