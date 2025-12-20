# Merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, l1, l2):
        l1 = deque(l1)
        l2 = deque(l2)

        merged = []
        while l1 and l2:
            if l1[0] < l2[0]:
                merged.append(l1.popleft())
            else:
                merged.append(l2.popleft())
        
        # merge remaining items of a list that still has items
        merged += l1
        merged += l2

        return merged

# T:O(n logn)
# S:O(n)