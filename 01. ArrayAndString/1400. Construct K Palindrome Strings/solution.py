# The critical observation is about characters with odd frequencies:
# - A palindrome can have at most one character with an odd count (which goes in the center)
# - If you have multiple characters with odd counts, each one must be the center of a different palindrome
# - Therefore, the number of odd-count characters determines the minimum number of palindromes you're forced to create

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        # edge case: if more palidromes expected than there are charachters in string
        if n < k:
            return False
    
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        # Count how many characters have an odd frequency
        odd_count = 0
        for c in count:
            if c % 2 != 0:
                odd_count += 1

        # 4. The number of odd-count characters must be less than or equal to k.
        # Each odd-count character must be the center of a different palindrome.
        return odd_count <= k
      
#T:O(n)
#S:O(1)