class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divider = 1
        while x >= 10 * divider:
            divider *= 10

        while x:
            left = x % 10
            right = x // divider

            if left != right:
                return False
            
            # Modify number
            # 1. remove left number
            x = x % divider
            # 2. remove right number
            x = x // 10

            divider = divider // 100
        
        return True

# T:O(log n)
# Finding the divider: O(log n) iterations
# Checking palindrome: O(log n) iterations

# S:O(1)
