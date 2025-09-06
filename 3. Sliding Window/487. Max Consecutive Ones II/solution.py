class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)

        max_count = 0
        zero_count = 0
        while r < n:
            if nums[r] == 0:
                zero_count += 1
                while zero_count > 1:
                    if nums[l] == 0:
                        zero_count -= 1
                    l += 1

            max_count = max(max_count, r - l + 1)
            r += 1

        return max_count

#T:O(n)
#S:O(1)