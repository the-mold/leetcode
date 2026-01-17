class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n

        # Each single iteration of this loop shifts all elements of the list one position to the right.
        for _ in range(k):
            prev = nums[-1]
            for j in range(n):
                nums[j], prev = prev, nums[j]

#T:O(k * n)
#S:O(1)