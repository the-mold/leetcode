#Intuition: anagram must be:
# - have the same length
# - have the same chars

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
          
        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        
        return freq_s == freq_t

#T:O(n)
#S:O(n)
