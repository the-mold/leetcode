class Solution:
    def check(self, nums: List[int]) -> bool:
        #  find array start
        start_idx = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                # found start candidate
                start_idx = i
                break

        # check that array is correctly rotated
        for i in range(1, len(nums)):
            curr_idx = (i + start_idx) % len(nums)
            prev_idx = (i - 1 + start_idx) % len(nums)
            if nums[curr_idx] < nums[prev_idx]:
                return False

        return True
      
# T:O(n)
# S:O(1)