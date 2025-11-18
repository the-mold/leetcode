class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        # 1. Sort the input array to group duplicates together.
        nums.sort()
        
        # 'used' array tracks which *indices* have been used.
        used = [False] * n

        def backtrack(curr_arr):
            if len(curr_arr) == n:
                res.append(list(curr_arr))
                return
            
            for i in range(n):
                # Condition 1: If this index has already been used in this path, skip.
                if used[i]:
                    continue
                
                # Condition 2: THE CRITICAL CHECK FOR DUPLICATES
                # If the current number is the same as the previous one,
                # AND the previous one hasn't been used yet in this level of recursion,
                # then we are about to start a duplicate path. So, we skip.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # --- Choose, Explore, Un-choose ---
                # Choose the number at index i
                used[i] = True
                curr_arr.append(nums[i])
                
                backtrack(curr_arr)
                
                curr_arr.pop()
                used[i] = False

        backtrack([])

        return res
    
# T:O(N * N log N)
# S:O(N) space of r recursion stack
