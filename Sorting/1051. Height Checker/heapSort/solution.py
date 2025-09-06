class Solution:
    # Function to max heapify a subtree (in top-down order) rooted at index i.
    def heapify(self, arr, n, i):
        # Initialize largest as root 'i'.
        largest, left, right = i, 2 * i + 1, 2 * i + 2

        # If the left child is larger than the root.
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If the right child is larger than the largest so far.
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root swap root with the largest element
        # Recursively heapify the affected sub-tree (i.e. move down).
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)
        # Build heap; heapify all elements except leaf nodes, in bottom-up order.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Traverse elements one by one, to move the current root to the end, and
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            # call max heapify on the reduced array.
            self.heapify(arr, i, 0)

    def heightChecker(self, heights: List[int]) -> int:
        # Sort the array using heap sort.
        sorted_heights = heights[:]
        self.heap_sort(sorted_heights)

        count = 0
        # Loop through the original and sorted arrays.
        for i in range(len(sorted_heights)):
            # Increment count if elements at the same index differ.
            if heights[i] != sorted_heights[i]:
                count += 1
        # Return the total count of differing elements.
        return count