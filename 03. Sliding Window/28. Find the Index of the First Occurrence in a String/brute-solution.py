class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        for idx, char in enumerate(haystack):
            if char == needle[0]:
                l = 1
                isSame = True
                while l < n:
        
                    if (idx+l) >= h or l >= n or haystack[idx+l] != needle[l]:
                        isSame = False
                        break

                    l += 1
                if isSame:
                    return idx
        
        return -1

#T:O(n*m)
#S:O(1)
