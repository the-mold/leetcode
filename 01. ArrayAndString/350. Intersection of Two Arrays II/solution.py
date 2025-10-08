# Note! Method is usefult when arrays are sorted!

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Finds the intersection of two lists.
    Each element in the result should appear as many times as it shows in both lists.
    """
    # Sort both lists to enable the two-pointer approach.
    nums1.sort()
    nums2.sort()
    
    # Initialize pointers for both lists and a list to store the result.
    i, j = 0, 0
    result = []
    
    # Iterate while both pointers are within the bounds of their respective lists.
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # If the element in nums1 is smaller, move its pointer forward.
            i += 1
        elif nums1[i] > nums2[j]:
            # If the element in nums2 is smaller, move its pointer forward.
            j += 1
        else:
            # If elements are equal, it's an intersection.
            # Add it to the result and move both pointers forward.
            result.append(nums1[i])
            i += 1
            j += 1
            
    return result

#T:O(n log n + m log m)
#S: from O(logn+logm) to O(n+m), depending on the implementation of the sorting algorithm. For the complexity analysis purposes, we ignore the memory required by inputs and outputs.

# Example Usage:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(f"The intersection is: {intersect(nums1, nums2)}")
# Expected output: [4, 9] or [9, 4]