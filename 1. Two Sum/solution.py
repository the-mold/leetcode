from typing import List

class Solution:
    # Solution 1: works but slow
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for idx, _ in enumerate(nums):
    #         for idx2, _ in enumerate(nums):
    #             if idx2 <= idx:
    #                 continue
    #             if (nums[idx] + nums[idx2]) == target:
    #                 return [idx, idx2]
    
    # # Solution 2
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     nums_map = {}
    #     for idx, n in enumerate(nums):
    #         complement = target - n
    #         if complement in nums_map:
    #             return [idx, nums_map[complement]]

    #         nums_map[n] = idx


    # Solution 3
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_s = set(nums)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_s and complement != nums[i]:
                return complement, nums[i]

    # Time: O(n)
    # Memory: O(n)
    