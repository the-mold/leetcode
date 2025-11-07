class Solution:
    def get_key(self, arr):
        res = ""
        for num in arr:
            res += str(num)
        
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n
        sett = set()

        def backtrack(curr_arr):
            
            if len(curr_arr) == n:
                key = self.get_key(curr_arr)
                if key not in sett:
                    sett.add(key)
                    res.append(list(curr_arr))
                    return
            
            for i in range(n):
                if used[i]:
                    continue
                
                used[i] = True

                curr_arr.append(nums[i])
                backtrack(curr_arr)
                curr_arr.pop()

                used[i] = False

        backtrack([])

        return res