class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1s = set(nums1)
        n2s = set(nums2)

        res = []
        for num in n1s:
            if num in n2s:
                res.append(num)

        return res
    
#T:O(n + m)
#S:O(n + m)
