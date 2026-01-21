class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        max_length = 0
        curr_length = 1
        prev = ord(s[0])
        for i in range(1, len(s)):
            curr = ord(s[i])
            if curr - prev == 1:
                curr_length += 1
            else:
                curr_length = 1
            
            max_length = max(max_length, curr_length)
            prev = curr

        return max_length

# T:O(n)
# S:O(1)