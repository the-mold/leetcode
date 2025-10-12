class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
            
            if mapping_s[s[i]] != t[i] or mapping_t[t[i]] != s[i]:
                return False
        
        return True
      
#T:O(n)
#S:O(2n) == O(n)
