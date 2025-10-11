class Solution:
    def backtracking(self, start, curr, nums):
        key = ",".join([str(dig) for dig in curr])
        if key not in self.set:
            self.res.append(curr.copy())
            self.set.add(key)

        for i in range(start, self.n):
            curr.append(nums[i])
            self.backtracking(i+1, curr, nums)
            curr.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.set = set()
        self.n = len(nums)
        self.backtracking(0, [], nums)
        return self.res