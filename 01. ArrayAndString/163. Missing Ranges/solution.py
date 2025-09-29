class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n == 0:
            ans.append([lower, upper])
            return ans
                    
        # add first elem
        if nums[0] > lower:
            ans.append([lower, nums[0] - 1])

        for i in range(n):
            # exit for the last element
            if i == n - 1:
                break
            
            num = nums[i]
            next_num = nums[i+1]
            if next_num - num <= 1:
                continue
            
            start = num + 1
            end = next_num - 1

            ans.append([start, end])

        # add last elem
        if nums[-1] < upper:
            ans.append([nums[-1]+1, upper])

        return ans
    