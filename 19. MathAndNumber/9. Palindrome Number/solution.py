class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverted_num = 0
        x_copy = x
        while x_copy != 0:
            right = x_copy % 10
            reverted_num = (reverted_num * 10) + right
            x_copy = x_copy // 10
        
        return x == reverted_num

# n = value of the input number

# T:O(logn), Number of digits in a number n is ⌊log(n)⌋ 
# Examples:
# n = 9 → 1 digit → log₁₀(9) ≈ 0.95 → ⌊0.95⌋ + 1 = 1
# n = 99 → 2 digits → log₁₀(99) ≈ 1.99 → ⌊1.99⌋ + 1 = 2
# n = 12321 → 5 digits → log₁₀(12321) ≈ 4.09 → ⌊4.09⌋ + 1 = 5


# S:O(1)

