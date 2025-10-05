class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Idea: 2*(a+b+c)−(a+a+b+b+c)=c
        #MAke set of numbers and multiple its sum by 2. This is what sum should be when 
        # all numbers are doubled. Substract the current sum and there is your answer - the missing number.
        return 2 * sum(set(nums)) - sum(nums)

# T:O(n)
# S:O(1)