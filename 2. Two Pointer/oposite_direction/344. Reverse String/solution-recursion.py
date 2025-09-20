class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(start,end,ls):
            if start >= end:
                return ls

            ls[start],ls[end] = ls[end],ls[start]

            helper(start+1,end-1, ls)

        return helper(0, len(s)-1, s)
    
#T:O(n)
#S:O(1)