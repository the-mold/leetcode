class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = k * 2 + 1
        res = [-1] * n

        if window_size > n:
            return res

        # calculate initial avarage value
        window_sum = sum(nums[0:window_size])
        res[k] = window_sum // window_size

        # calculate all other values
        for i in range(k+1, n-k):
            # recalculate window sum by substracting last element(on the left) and adding a new one(on the right)
            window_sum = window_sum - nums[i - k - 1] + nums[i + k]
            res[i] = window_sum // window_size
        
        return res
    
#T:O(n)
#S:O(1)