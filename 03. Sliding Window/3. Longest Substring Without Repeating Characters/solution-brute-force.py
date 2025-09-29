class Solution:
    def is_unique_in_range(self, s, start, end):
        chars = set()
        
        for i in range(start, end + 1):
            char = s[i]
            if char in chars:
                return False
            chars.add(char)
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_unique_in_range(s, i, j):
                    result = max(result, j - i + 1)
        
        return result