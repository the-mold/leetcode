class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # need to sort to skip duplicates
        candidates.sort()
        return self._combinationSum2(candidates, target)

    def _combinationSum2(self, candidates: List[int], target: int):
        if target == 0:
            return [[]]

        if target < 0 or not candidates:
            return []

        first = candidates[0]
        combos_with_first = []
        for combs in self.combinationSum2(candidates[1:], target - first):
            combos_with_first.append([first, *combs])

        # skip all duplicates
        j = 0
        while len(candidates) > j and candidates[j] == first:
            j += 1
        combos_without_first = self.combinationSum2(candidates[j:], target)

        return combos_with_first + combos_without_first
      
# T:O(2**n)
# S:O(2**n)
