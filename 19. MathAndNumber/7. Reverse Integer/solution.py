class Solution:
    def reverse(self, x: int) -> int:

        # Set limits [-2**31, 2**31 - 1], as stated in the problem
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1
        if x < 0:
            sign = -1
        
        reversed_num = 0
        x = abs(x)
        while x != 0:
            # get last digit 
            digit = x % 10

            # Check for overflow BEFORE the multiplication/addition
            # For positive numbers, the max reversed value is INT_MAX (ends in 7)
            if sign == 1 and (reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7)):
                return 0
            
            # For negative numbers, the max reversed absolute value is abs(INT_MIN) (ends in 8)
            if sign == -1 and (reversed_num > abs(INT_MIN) // 10 or (reversed_num == abs(INT_MIN) // 10 and digit > 8)):
                return 0

            reversed_num = (reversed_num * 10) + digit
            # remove last digit in a number. Divide it by 10 and take floor of result.
            x //= 10
    
        return sign * reversed_num


# Note! The part with
# ```
# (reversed_num == INT_MAX // 10 and digit > 7)
# ```
# is just checking for the last allowed digits. Out limit is 2**31-1 = 2,147,483,647.
# So when you are adding the last digit:
# If digit is 7, the result is 2,147,483,647 (which is valid).
# If digit is 8, the result would be 2,147,483,648 (which is an overflow).
# If digit is 9, the result would be 2,147,483,649 (which is an overflow).