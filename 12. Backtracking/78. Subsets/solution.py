class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.n = len(nums)
        self.backtracking(0, [], nums)
        return self.output

    def backtracking(self, start, curr, nums):
        self.output.append(curr.copy())

        for i in range(start, self.n):
            curr.append(nums[i])
            self.backtracking(i+1, curr, nums)
            curr.pop()

#T:O(n * 2**N)  to generate all subsets and then copy them into the output list.
#S:O(n) We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking. Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, so the output array is ignored.


#input [1,2,3]

# Call backtracking(0, [])
# - append []                  -> output: [ [] ]
# - i=0 -> curr=[1]
#   Call backtracking(1, [1])
#   - append [1]               -> output: [ [], [1] ]
#   - i=1 -> curr=[1,2]
#     Call backtracking(2, [1,2])
#     - append [1,2]           -> output: [ [], [1], [1,2] ]
#     - i=2 -> curr=[1,2,3]
#       Call backtracking(3, [1,2,3])
#       - append [1,2,3]       -> output: [ [], [1], [1,2], [1,2,3] ]
#       - (no loop, start=3)
#       Return; pop -> curr=[1,2]
#     - end i=2
#     Return; pop -> curr=[1]
#   - i=2 -> curr=[1,3]
#     Call backtracking(3, [1,3])
#     - append [1,3]           -> output: [ [], [1], [1,2], [1,2,3], [1,3] ]
#     - (no loop)
#     Return; pop -> curr=[1]
#   - end i=1..2
#   Return; pop -> curr=[]
# - i=1 -> curr=[2]
#   Call backtracking(2, [2])
#   - append [2]               -> output: [ [], [1], [1,2], [1,2,3], [1,3], [2] ]
#   - i=2 -> curr=[2,3]
#     Call backtracking(3, [2,3])
#     - append [2,3]           -> output: [ [], [1], [1,2], [1,2,3], [1,3], [2], [2,3] ]
#     - (no loop)
#     Return; pop -> curr=[2]
#   - end
#   Return; pop -> curr=[]
# - i=2 -> curr=[3]
#   Call backtracking(3, [3])
#   - append [3]               -> output: [ [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3] ]
#   - (no loop)
#   Return; pop -> curr=[]
# Return