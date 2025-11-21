class Solution:
    def __init__(self):
        # Tracks the total number of ways to reach the target
        self.total_ways = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.calculate_ways(nums, 0, 0, target)
        return self.total_ways

    def calculate_ways(
        self, nums: List[int], current_index: int, current_sum: int, target: int
    ):
        if current_index == len(nums):
            # Check if the current sum matches the target
            if current_sum == target:
                self.total_ways += 1
        else:

            # Include the current number with a positive sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
            )

            # Include the current number with a negative sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
            )