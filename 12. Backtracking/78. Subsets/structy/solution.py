class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        subsets_without_first = self.subsets(nums[1:])

        subsets_with_first = []
        for sub in subsets_without_first:
            subsets_with_first.append([first, *sub])

        return subsets_without_first + subsets_with_first
      
# T:O(2**n)
# S:O(2**n)