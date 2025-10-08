class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freq = {}
        for n in nums1:
            freq[n] = freq.get(n, 0) + 1

        res = []
        for n in nums2:
            if n in freq and freq[n] > 0:
                res.append(n)
                freq[n] -= 1
                
        return res