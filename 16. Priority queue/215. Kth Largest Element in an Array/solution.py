import heapq

def findKthLargest(nums, k):
  min_heap = []

  for num in nums:
    print("----num ", num)
    heapq.heappush(min_heap, num)
    print("min_heap before remove ", min_heap)
    if len(min_heap) > k:
      heapq.heappop(min_heap)
    
    print("min_heap after remove ", min_heap)
  
  return min_heap[0]  # Root of min-heap is the k-th largest element

#T: O(n log k)
#S: O(k)

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))  # Output: 5



# Intuition
# You start pushing elements to the min heap(lowest elements will be first in your array). If size of array exceeds k, then pop element from heap. In this way
# the first element in the array will always be your kth largest element. 