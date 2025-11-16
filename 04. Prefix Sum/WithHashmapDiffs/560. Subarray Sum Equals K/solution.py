class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        count = 0
        prefixSums = defaultdict(int)
        
        prefixSums[0] = 1

        for num in nums:
            currSum += num

            diff = currSum - k
            if diff in prefixSums:
                #Why Frequency Matters
                #If prefix_sum - k appears multiple times in our history, it means there are multiple different subarrays ending at the current position with sum = k.
                count += prefixSums[diff]

            # The frequency tells us HOW MANY different starting positions can form a valid subarray ending at the current position.
            prefixSums[currSum] += 1

        return count
    
#T:O(n)
#S:O(1)


# How It Works
# Example 1: nums = [1,1,1], k = 2

# Index	num	prefix_sum	prefix_sum - k	count	sum_freq
# -	-	0	-	0	{0: 1}
# 0	1	1	-1	0	{0: 1, 1: 1}
# 1	1	2	0	1	{0: 1, 1: 1, 2: 1}
# 2	1	3	1	2	{0: 1, 1: 1, 2: 1, 3: 1}
# Valid subarrays:

# [1,1] (indices 0-1): prefix_sum[1]=2, prefix_sum[-1]=0, diff=2 ✅
# [1,1] (indices 1-2): prefix_sum[2]=3, prefix_sum[0]=1, diff=2 ✅
# Output: 2 ✅

# Example 2: nums = [1,2,3], k = 3

# Index	num	prefix_sum	prefix_sum - k	count	sum_freq
# -	-	0	-	0	{0: 1}
# 0	1	1	-2	0	{0: 1, 1: 1}
# 1	2	3	0	1	{0: 1, 1: 1, 3: 1}
# 2	3	6	3	2	{0: 1, 1: 1, 3: 1, 6: 1}
# Valid subarrays:

# [1,2] (indices 0-1): sum = 3 ✅
# [3] (index 2): sum = 3 ✅
# Output: 2 ✅

# Why This Works
# Prefix sum trick: sum(nums[i:j+1]) = prefix_sum[j] - prefix_sum[i-1]
# Target: We want prefix_sum[j] - prefix_sum[i-1] = k
# Rearrange: prefix_sum[i-1] = prefix_sum[j] - k
# Count: For each j, count how many previous positions had prefix_sum = current_sum - k
# Edge Cases
# k = 0: Counts subarrays with sum 0
# Negative numbers: Works correctly (unlike sliding window)
# Multiple subarrays with same sum: Hash map tracks frequency
