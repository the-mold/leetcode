class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # early exit of you are out of bound for some word
                if i == len(s):
                    return res
                
                # exit if you find a different char in some word
                if s[i] != strs[0][i]:
                    return res
            
            # otherwise append char to the result
            res += strs[0][i]
        
        return res
    
 # n - number of words
 # m - length of word checked   
    
# T:O(mn)
# S:O(1)