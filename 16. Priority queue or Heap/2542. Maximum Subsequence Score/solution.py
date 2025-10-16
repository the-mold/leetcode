class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums2)
        indexes = list(range(n))

        indexes.sort(key=lambda x: nums2[x], reverse=True)

        heap = []
        max_sum = 0
        current_sum = 0

        for idx in indexes:
            n1 = nums1[idx]
            n2 = nums2[idx]

            current_sum += n1
            heapq.heappush(heap, n1)

            if len(heap) > k:
                min_number = heapq.heappop(heap)
                current_sum -= min_number
            
            if len(heap) == k:
                max_sum = max(max_sum, current_sum * n2)
        
        return max_sum
      
#T:O(n log n)
#S:O(n)