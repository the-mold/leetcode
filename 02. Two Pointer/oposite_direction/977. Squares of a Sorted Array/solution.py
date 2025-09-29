from types import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l = 0
        r = n - 1

        # if you so reverse loop and because input is sorted, you cover
        # number from smallest(negative) to largest(positive). Square of either of this
        # numbers should be added to the end of result array.
        for i in range(n-1,-1,-1):
            if abs(nums[l]) < abs(nums[r]):
                number_to_squar = nums[r]
                r -= 1
            else:
                number_to_squar = nums[l]
                l += 1

            # push the largest element to the back of the result array
            res[i] = number_to_squar ** 2
        
        return res
      
# T: O(n)
# S: O(n)