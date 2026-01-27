class Solution:
    def merge(self, arr1, arr2):
        q1 = collections.deque(arr1)
        q2 = collections.deque(arr2)

        res = []
        while q1 and q2:
            if q1[0] < q2[0]:
                res.append(q1.popleft())
            else:
                res.append(q2.popleft())

        if q1:
            res = res + list(q1)
        if q2:
            res = res + list(q2)

        return res

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self.merge(nums1, nums2)
        print(arr)
        #[1, 2, 3]
        mid = len(arr) // 2
        if len(arr) % 2 == 1:
            return arr[mid]
        else:
             #[1, 2, 2, 3]
            return (arr[mid-1] + arr[mid]) / 2
        
# T:O(n + m)
# S:O(n + m)