class Solution:
    def bubble_sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.bubble_sort(sorted_heights)

        ans = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                ans +=1
        
        return ans 
      
# T:O(n**2)
# S:O(n)


# Intuition

# Bubble sort: in each interration move the largest element to the end.

# 1. The Outer Loop: for i in range(n - 1)
# - Purpose: This loop controls the number of "passes" we make over the array.
# - How it works: After each complete pass, the next largest element "bubbles up" to its correct final position at the end of the unsorted portion of the array.
# - After the 1st pass (i=0), the largest element (8) is guaranteed to be at the very end.

# 2. The Inner Loop: for j in range(n - i - 1)
# - Purpose: This loop performs the actual comparisons and swaps for a single pass. It moves through the array from left to right, comparing adjacent elements.
# - Why n - i - 1? (The Optimization): This is the most important part. After i passes of the outer loop, the last i elements are already sorted and in their final positions. We don't need to check them again. 
# This `- i`` part makes the inner loop shorter and shorter with each pass, saving unnecessary comparisons.
