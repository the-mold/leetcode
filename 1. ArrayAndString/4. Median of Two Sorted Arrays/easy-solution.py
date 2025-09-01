class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        res = []
        def merge():
            nonlocal p1,p2

            if p1 < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    res.append(nums1[p1])
                    p1 +=1 
                else:
                    res.append(nums2[p2])
                    p2 +=1
            elif p2 == n:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 +=1


        for i in range(m + n):
            merge()

        mid = (n+m) // 2
        if (m+n) % 2 == 0:
            # even
            return (res[mid] + res[mid - 1]) / 2
        else:
            # odd
            return res[mid]
        
# T:O(n)
# S:O(n)