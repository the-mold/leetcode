# NOTE: the trick is not to decrease number of candidates in the first loop.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        if not candidates or target < 0:
            return []

        first = candidates[0]
        combo_with_first = []
        for combo in self.combinationSum(candidates, target - first):
            combo_with_first.append([first, *combo])

        combo_without_first = self.combinationSum(candidates[1:], target)

        return combo_with_first + combo_without_first
      
# T:O(n**2)
# S:O(n**2)
