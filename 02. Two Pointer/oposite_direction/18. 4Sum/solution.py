class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # WARNING! DO not forget to sort!!!
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                lo = j + 1
                hi = n - 1

                while lo < hi:
                    local_sum = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if local_sum > target:
                        hi -= 1
                    elif local_sum < target:
                        lo += 1
                    else:
                        # there is match
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1

                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                        
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -= 1

        return res
      
      
#T:O(n**3)
#S:O(n), because of sorting