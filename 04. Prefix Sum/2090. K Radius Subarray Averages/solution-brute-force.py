class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        divisor = k * 2 + 1
        for i in range(n):
            start = i - k
            if i - k < 0:
                res.append(-1)
                continue

            end = i + k
            if i + k >= n:
                res.append(-1)
                continue

            subarr_sum = sum(nums[start:end+1])
            res.append(subarr_sum // divisor) 
        
        return res
    
# T:O(n**2)
# S:O(n)