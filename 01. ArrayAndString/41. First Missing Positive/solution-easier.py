class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        seen = set(nums)

        # you loop through all possible answers. You start with 1 and finish with n.
        # Because in array of size n, the max answer can be n.
        # Example: [1,2,0] -> 3
        #          [1,2,3,0] -> 4
        for i in range(1, n + 1):
            if i not in seen:
                return i 

        # if no answer was found, it means that array contains a sequence for 1 to n with no gaps. Return n+1
        return n+1

# T:O(n)
# S:O(n)
