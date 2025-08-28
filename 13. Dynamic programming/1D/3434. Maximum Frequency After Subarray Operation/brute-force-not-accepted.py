class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_count = 0
        for num in nums:
            if num == k:
                max_count += 1

        for i in range(n):
            for j in range(i, n):
                for subarray_idx in range(i, j+1):
                    x = k - nums[subarray_idx]

                    new_count = 0
                    for idx in range(n):
                        if idx < i or idx > j:
                            if nums[idx] == k:
                                new_count +=1
                    
                    for idx in range(i, j+1):
                        if (nums[idx] + x) == k:
                            new_count +=1

                    if new_count > max_count:
                        max_count = new_count
        
        return max_count
  