class Solution:
    def counting_sort(self, arr):
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        max_val = max(arr)
        min_val = min(arr)

        idx_to_update = 0
        for i in range(min_val, max_val + 1):
            while i in counts and counts[i] > 0:
                arr[idx_to_update] = i
                counts[i] -= 1
                idx_to_update += 1

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.counting_sort(sorted_heights)

        ans = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                ans +=1
        
        return ans 

# Time complexity: O(n+k)

# We iterate on the array elements while counting the frequency and finding minimum and maximum values, taking O(n) time.
# Then we iterate on the input array's element's range, which will take O(k) time. Thus, sorting will take O(n+k) time.
# While comparing sorted and unsorted arrays, we again iterate on n elements, which will take O(n) time.
# Thus, overall it takes O(n+n+k)=O(n+k) time.
# Space complexity: O(n)

# We use a hash map counts which might store all O(n) elements of the input array in worst-case.
# We created an additional array sortedHeights of size n.
# Thus, overall we use O(n) space.