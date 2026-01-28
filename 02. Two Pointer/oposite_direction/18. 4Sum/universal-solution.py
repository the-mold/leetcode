class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # WARNING! DO not forget to sort!!!
        nums.sort()
        res = []
        local_nums = []
        n = len(nums)

        def kSum(k, start, target_number):
            if k != 2:
                for i in range(start, n):
                    # skip the duplicates
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    
                    local_nums.append(nums[i])
                    kSum(k - 1, i + 1, target_number - nums[i])
                    local_nums.pop()
            else:
                lo = start
                hi = n - 1
                while lo < hi:
                    local_sum = nums[lo] + nums[hi]
                    if local_sum > target_number:
                        hi -= 1
                    elif local_sum < target_number:
                        lo += 1
                    else:
                        # found a match
                        res.append(local_nums + [nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1

                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                        
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

        kSum(4, 0, target)
        return res

# T:O(n**3)
# S:O(n)