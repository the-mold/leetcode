class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n
        sett = set()
        nums.sort()

        def backtrack(curr_arr):
            
            if len(curr_arr) == n:
                res.append(list(curr_arr))
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                # To avoid duplicates.
                # If the current element is the same as the previous one,
                # AND the previous one has NOT been used yet in this path,
                # then skip the current element.
                # This ensures that for a group of duplicate numbers, we always
                # pick them in the order they appear in the sorted array.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True

                curr_arr.append(nums[i])
                backtrack(curr_arr)
                curr_arr.pop()

                used[i] = False

        backtrack([])

        return res