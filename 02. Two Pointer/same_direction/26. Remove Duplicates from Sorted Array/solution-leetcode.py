class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        left_idx = 0

        for n in range(1, len(nums)):
            if nums[left_idx] != nums[n]:
                nums[count] = nums[n]
                count += 1
                left_idx = n

        return count
