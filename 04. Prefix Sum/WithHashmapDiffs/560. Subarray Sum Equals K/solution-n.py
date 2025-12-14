# Note: to get here step by step start with n**3 and after n**2 solution.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)

        count = 0
        seen = collections.defaultdict(int)
        for num in prefix:
            complement = num - k

            #check if complement in seen.
            # seen[complement] tells us how many previous prefix sums equal the value we need
            # Each occurrence represents a different starting position for a valid subarray
            # If we've seen the same prefix sum multiple times, we can form multiple subarrays ending at the current position
            if complement in seen:
                count += seen[complement]
            
            # increment count of sums that we checked already
            seen[complement] += 1

        return count

# T:O(n)
# S:O(n)


# Example:
# numbers =    [1, 2, -1, 3], target_sum = 2
# prefix_sum = [0, 1,  3, 2, 5]

# Step 1: num=0, complement=0-2=-2, seen={}, count=0
#         seen = {0: 1}

# Step 2: num=1, complement=1-2=-1, seen={0:1}, count=0  
#         seen = {0: 1, 1: 1}

# Step 3: num=3, complement=3-2=1, seen={0:1, 1:1}, count=0+1=1
#         (Found subarray [2] with sum 2)
#         add seen[complement] to count
#         seen = {0: 1, 1: 1, 3: 1}

# Step 4: num=2, complement=2-2=0, seen={0:1, 1:1, 3:1}, count=1+1=2
#         (Found subarray [1,2,-1] with sum 2)
#         add seen[complement] to count
#         seen = {0: 1, 1: 1, 3: 1, 2: 1}

# Step 5: num=5, complement=5-2=3, seen={0:1, 1:1, 3:1, 2:1}, count=2+1=3
#         (Found subarray [-1,3] with sum 2)
#         add seen[complement] to count
#         seen = {0: 1, 1: 1, 3: 1, 2: 1, 5:1}