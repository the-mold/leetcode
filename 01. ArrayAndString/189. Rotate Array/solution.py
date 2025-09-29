class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # normalize k if it k>n. For example if array length is 5 and k is 10, then normalized k is k % n = 5.
        k = k % n

        temp = nums.copy()

        for i in range(n):
            idx = (i + k) % n
            nums[idx] = temp[i]
  
# T:O(n)
# S:O(n)