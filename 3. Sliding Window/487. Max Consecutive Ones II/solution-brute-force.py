class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0

        zero_count = 0
        for i in range(len(nums)):
            zero_count = 0
            for j in range(i, len(nums)):
                if zero_count == 2:
                    break
                if nums[j] == 0:
                    zero_count += 1
                
                if zero_count <= 1:
                    max_count = max(max_count, j - i + 1)
        
        return max_count

#T:O(n**2)
#S:O(1)
