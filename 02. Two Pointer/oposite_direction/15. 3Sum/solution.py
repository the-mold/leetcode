class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # break the loop here. If you reached positive numbers in sorted array, there is no way you can find 3 numbers that add up to 0
            if nums[i] > 0:
                break
            
            # skip duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue

            # now start two sum with pointers
            l, r = i + 1, len(nums) - 1

            while l < r:
                local_sum = nums[i] + nums[l] + nums[r]
                if local_sum < 0:
                    l += 1
                elif local_sum > 0:
                    r -= 1
                else:
                    # we found a match
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1 
                    r -= 1

                    # skip duplicates for l
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    
                    # skip duplicates for r
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
            
        return res
    
#T:O(n log n + n^2) => O(n^2)
#S:O(n log n)
