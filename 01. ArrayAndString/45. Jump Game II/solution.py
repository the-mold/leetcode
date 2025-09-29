class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # your current jump reach
        curr_reach = 0
        # maximum reach that you counl reach if you check all possible values in your current jump reach
        far_reach = 0

        count = 0

        # loop is to check every index. You not jumping with i. `i` just checks every possiblility within your current jump reach
        for i in range(n-1):
            far_reach = max(far_reach, i + nums[i])

            # you have to make a jump here. You make a jump to the furthest point that you found.
            if i == curr_reach:
                count += 1
                curr_reach = far_reach
    
        return count

#T:O(n)
#S:O(1)
