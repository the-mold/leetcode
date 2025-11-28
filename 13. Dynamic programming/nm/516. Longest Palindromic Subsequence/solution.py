class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self._longestPalindromeSubseq(s, 0, len(s) - 1, {})

    def _longestPalindromeSubseq(self, s, start, end, memo):
        key = (start, end)
        if key in memo:
            return memo[key]

        # if both point at the same letter, return 1. String of length 1 is always a palidrome.
        if start == end:
            return 1

        if start > end:
            return 0

        res = None
        if s[start] == s[end]:
            res = 2 + self._longestPalindromeSubseq(s, start+1, end-1, memo)
        else:
            res = max(self._longestPalindromeSubseq(s, start+1, end, memo), self._longestPalindromeSubseq(s, start, end-1, memo))

        memo[key] = res
        return res

#s = length of string

# T:O(s**2)
# S:O(s**2)
