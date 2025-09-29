class Solution:
    # Bucket sort function for each place value digit.
    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]

        # Store the respective number based on its digit.
        for val in arr:
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)

        # Overwrite 'arr' in sorted order of current place digits.
        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                arr[index] = val
                index += 1

    # Radix sort function.
    def radix_sort(self, arr):
        # Find the absolute maximum element to find max number of digits.
        max_element, max_digits = max(abs(val) for val in arr), 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10

        # Radix sort, least significant digit place to most significant.
        place_value = 1
        for _ in range(max_digits):
            self.bucket_sort(arr, place_value)
            place_value *= 10

    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array using radix sort.
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count
      
# Time complexity: O(d⋅(n+b))

# We iterate on the array elements to find the maximum number and then find the count of its digits, taking O(n+d) time.
# Then we sort the array for each integer place which will take O(n+b) time, thus for all d places it will take O(d⋅(n+b)) time. Thus, sorting will take O((n+d)+d⋅(n+b))=O(d⋅(n+b)) time.
# While comparing sorted and unsorted arrays, we again iterate on n elements, which will take O(n) time.
# Therefore, overall it takes O(n+d⋅(n+b))=O(d⋅(n+b)) time.
# Space complexity: O(n+b)

# We create an additional array sortedHeights of size n and buckets which use O(n+b) space.
# Thus, overall we use O(n+b) space.