class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
 
        ans = ""
        count = 0
        for i in range(len(s)-1, -1,-1):
            char = s[i].upper()

            ans += char
            count += 1
            if count == k and i != 0:
                ans += "-"
                count = 0
        
        return ans[::-1]

# T:O(n)
# S:O(1)
