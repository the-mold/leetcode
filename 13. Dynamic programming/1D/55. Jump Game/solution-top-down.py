class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def can_reach(position):
            # Base case 1: We successfully reached the last index.
            if position >= n - 1:
               return True
            
            if position in memo:
                return memo[position]
        
            max_jump = nums[position]
            # try evey possible length of the current jump
            for jump in range(1, max_jump + 1):
                # return if i can reach end position(base case) from the current position
                if can_reach(jump + position):
                    memo[position] = True
                    return True
            
            # If no jump from this position worked, it's a dead end.
            memo[position] = False
            return False

        return can_reach(0)

#T:(n**2)
#S:(n)