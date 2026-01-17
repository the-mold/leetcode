class Solution:
    def reverse_array_between_indexes(self, nums, left, right):
        l = left
        r = right
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # reverse whole array
        self.reverse_array_between_indexes(nums, 0, n - 1)

        # reverse left part
        self.reverse_array_between_indexes(nums, 0, k - 1)

        # reverse right part
        self.reverse_array_between_indexes(nums, k, n - 1)
        
# T:O(n)
# S:O(1)
