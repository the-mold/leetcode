class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        
        return count

# T: O(n * log(m)), where log(m) is time needed to convert each number with length m to string
# S: O(log(m)) store string number temporarily 
