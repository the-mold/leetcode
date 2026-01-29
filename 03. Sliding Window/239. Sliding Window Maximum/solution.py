# Intuition:
# maintain dq with the monotonique queue of array indexes. When you consider another element,
# pop all indexes from dq values of which are less than the new element. In this way the very first item in dq[0]
# is the current maximum.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return max(nums)

        dq = deque()
        res = []
        
        for i in range(k):
            # remove all previous elements that are less than the current element
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            # remove the element that is currently not in the window frame. There can be maximum one element like this in queue and
            # it is in the beginning of the dq if it exists.
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # remove all previous elements that are less than the current element
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]])
        
        return res

#T:O(n)
#S:O(k)