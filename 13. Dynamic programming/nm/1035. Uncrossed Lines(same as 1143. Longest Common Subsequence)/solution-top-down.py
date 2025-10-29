class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        n1 = len(nums1)
        n2 = len(nums2)

        def solve(i, j):
            if i >= n1 or j >= n2:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if nums1[i] == nums2[j]:
                res = 1 + solve(i + 1, j + 1)
            else:
                res = max(solve(i+1,j), solve(i,j+1))

            memo[(i,j)] = res
            return res
        
        return solve(0, 0)