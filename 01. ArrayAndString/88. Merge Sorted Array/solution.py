class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_p = m-1
        nums2_p = n - 1
        for i in range(len(nums1)-1, -1, -1):
            if nums1_p < 0:
                nums1[i] = nums2[nums2_p]
                nums2_p -= 1
            elif nums2_p < 0:
                nums1[i] = nums1[nums1_p]
                nums1_p -= 1
            elif nums1[nums1_p] > nums2[nums2_p]:
                nums1[i] = nums1[nums1_p]
                nums1_p -= 1
            else:
                nums1[i] = nums2[nums2_p]
                nums2_p -= 1

#T:O(n)
#S:O(1)
