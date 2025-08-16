class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        result = ""
        group_idx = 0

        while num > 0:
            part = num % 1000

            if part != 0:
                group_result = ""

                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100
                
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                if part > 0:
                    group_result += ones[part] + " "
                
                group_result += thousands[group_idx] + " "
                result = group_result + result
            
            num //= 1000
            group_idx += 1
        
        return result.strip()
    
# Time Complexity: O(log N)
# The time complexity is O(log N), where N is the value of the input number num.

# Reasoning:

# The dominant part of the algorithm is the while num > 0: loop.
# In each iteration of the loop, the number num is divided by 1000 (num //= 1000).
# This means the number of times the loop runs is proportional to the number of three-digit "groups" in the input number. For example:
# 123 runs once.
# 123,456 runs twice.
# 123,456,789 runs three times.
# The number of digits in a number N is mathematically represented as log₁₀(N). Since we are processing in chunks of 1000, the number of iterations is proportional to log₁₀₀₀(N), which is just a constant factor different from log(N).
# All operations inside the loop (like modulo, division, and array lookups) take a constant amount of time because they operate on a number (part) that is always less than 1000.
# Therefore, the runtime grows logarithmically with the size of the input number N.

# Space Complexity: O(log N)
# The space complexity is also O(log N).

# Reasoning:

# The space used by the ones, tens, and thousands arrays is constant. It doesn't change no matter how big the input number is.
# The primary user of space is the result string.
# The length of the final result string is proportional to the number of words needed to represent the number, which in turn is proportional to the number of digits in num.
# As we established, the number of digits is log(N).