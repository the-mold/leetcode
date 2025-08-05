from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges nums2 into nums1 as one sorted array, in-place.
    The function modifies nums1 directly and does not return anything.
    
    This solution works backwards from the end of the arrays to avoid overwriting
    elements that still need to be sorted. It runs in O(m + n) time and O(1) space.
    """
    # Pointer for the last element of the initial part of nums1
    p1 = m - 1
    # Pointer for the last element of nums2
    p2 = n - 1
    # Pointer for the last position in the merged nums1 array
    p_merge = m + n - 1

    # Loop backwards as long as there are elements in both arrays to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merge] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merge] = nums2[p2]
            p2 -= 1
        p_merge -= 1

    # If there are any remaining elements in nums2 (because all elements in
    # nums1 were larger), copy them to the front of nums1.
    # No need to handle remaining elements in nums1, as they are already in place.
    while p2 >= 0:
        nums1[p_merge] = nums2[p2]
        p2 -= 1
        p_merge -= 1

# T: O(n)
# S: O(1)


# Why loop over p2 additionally?
# The reason we only need to check for remaining elements in nums2 is because of where we are putting the final, sorted elements.
# Let's think about the state of the nums1 array when the main loop (while p1 >= 0 and p2 >= 0:) finishes.

# Scenario 1: The loop ends because we've used all of nums2 (p2 < 0).
# This means all the elements from nums2 have been successfully merged into the end of nums1.
# The elements that are left over are in the beginning of nums1 (from index 0 to p1).
# Since both original arrays were sorted, these leftover nums1 elements are guaranteed to be smaller than any of the elements we've already moved.
# Crucially, they are already in their correct final sorted positions. We are building the sorted array inside nums1, and its smallest elements naturally belong at the start. We don't need to move them or do anything else with them.

# Scenario 2: The loop ends because we've used all of the original nums1 elements (p1 < 0).
# This means there are still elements left over in nums2 (from index 0 to p2).
# These elements are smaller than all the elements we have already placed at the end of nums1.
# However, these elements are currently sitting in the nums2 array. They are not yet in their correct final positions, which are the empty slots at the beginning of the nums1 array.
# Therefore, we must have a loop to copy these remaining elements from nums2 into the front of nums1.
# In short: Any leftover elements from nums1 are already in the correct place. Any leftover elements from nums2 are not, so we have to copy them over. This is a key benefit of merging from back to front.
