class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)

        greatness = 0
        r = 0

        # loop the array from left to right. For every smallest value(because array is sorted) you will look for a value that is greater than it(r index while loop)
        for l in range(len(nums_sorted)):
            curr_num = nums_sorted[l]

            # find the first element that is greater than current element
            while r < len(nums_sorted) and nums_sorted[r] <= curr_num:
                r += 1

            if r < len(nums_sorted):
                greatness += 1
                r += 1

        return greatness

# T:O(n logn) because of sorting
#Note! Event though there is a nested `while` look the overal complexity of both loops is O(n) because the r moves only forward and never resets.

# S:O(n) because of sorting
