from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    if len(nums) < k:
        return max(nums)
    q = deque(nums[:k])
    res = []
    res.append(max(q))

    for i in range(k, len(nums)):
        q.popleft()
        q.append(nums[i])
        res.append(max(q))
    
    return res

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)