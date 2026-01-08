class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        return self._findLongestChain(pairs, 0, float("-inf"), {})

    def _findLongestChain(self, pairs, idx, prev_end, memo):
        if idx == len(pairs):
            return 0

        key = (idx, prev_end)
        if key in memo:
            return memo[key]

        candidate = pairs[idx]
        not_take = self._findLongestChain(pairs, idx+1, prev_end, memo)
        take = 0
        if prev_end < candidate[0]:
            take = 1 + self._findLongestChain(pairs, idx+1, candidate[1], memo)

        res = max(take, not_take)
        memo[key] = res
        return res

# T:O(nlogn + n**2) => O(n**2)
# S:O(n**2)