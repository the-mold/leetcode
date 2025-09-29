class Solution:
    # Function to merge two sub-arrays in sorted order.
    def merge(self, arr, left, mid, right, temp_arr):
        # Calculate the start and sizes of two halves.
        start1 = left
        start2 = mid + 1
        n1 = mid - left + 1
        n2 = right - mid

        # Copy elements of both halves into a temporary array.
        for i in range(n1):
            temp_arr[start1 + i] = arr[start1 + i]
        for i in range(n2):
            temp_arr[start2 + i] = arr[start2 + i]

        # Merge the sub-arrays in 'temp_arr' back into the original array 'arr' in sorted order.
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                arr[k] = temp_arr[start1 + i]
                i += 1
            else:
                arr[k] = temp_arr[start2 + j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < n1:
            arr[k] = temp_arr[start1 + i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = temp_arr[start2 + j]
            j += 1
            k += 1

    # Recursive function to sort an array using merge sort.
    def merge_sort(self, arr, left, right, temp_arr):
        if left >= right:
            return
        mid = (left + right) // 2
        # Sort first and second halves recursively.
        self.merge_sort(arr, left, mid, temp_arr)
        self.merge_sort(arr, mid + 1, right, temp_arr)
        # Merge the sorted halves.
        self.merge(arr, left, mid, right, temp_arr)

    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array using merge sort.
        sorted_heights = heights[:]
        temp_arr = [0] * len(heights)
        self.merge_sort(sorted_heights, 0, len(sorted_heights) - 1, temp_arr)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count
  
# Time complexity: O(nlogn)
# While sorting, we divide the arr array into two halves till there is only one element in the array, which will lead to O(logn) steps.
# n→n/2→n/4→...→1 (k steps)
# (n/2)**(k−1) =1⟹ k≈logn
# After each division, we merge those respective halves which will take O(n) time each. Thus, sorting will take O(nlogn) time.
# While comparing sorted and unsorted arrays, we again iterate on n elements, which will take O(n) time.
# Thus, overall it takes O(n+nlogn)=O(nlogn) time.
# Space complexity: O(n)

# The recursive stack will take O(logn) space, and we used additional arrays, temporaryArray and sortedHeights of size n each.
# Thus, overall we use O(logn+2n)=O(n) space.
