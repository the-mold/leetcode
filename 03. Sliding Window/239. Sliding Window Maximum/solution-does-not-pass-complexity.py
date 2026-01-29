import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        for i in range(len(nums)):
            q.append(nums[i])

            if len(q) == k:
                res.append(max(q))
                q.popleft()
        
        return res

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

#T:O(n)
#S:O(k), we need space for k elems in the deque. Because k is constant, we can say that space complexity is O(1)
