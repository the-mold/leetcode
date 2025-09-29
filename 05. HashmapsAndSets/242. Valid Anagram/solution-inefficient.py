class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
#T:O(n log n + n log n + n) => O(n log n)   where each `n log n` is soring and `+n` is comparing of two arrays.
#S:O(n)