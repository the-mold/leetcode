class Solution:
    def generate_rle(self, current):
        result = []
        count = 1
        curr_string = current[0]

        for i in range(1, len(current)):
            if current[i] == curr_string:
                count += 1
            else:
                result.append(str(count) + curr_string)
                curr_string = current[i]
                count = 1
        
        # append the last string
        result.append(str(count) + curr_string)
        
        return "".join(result)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        current = "1"
        for i in range(2, n + 1):
            current = self.generate_rle(current)
        
        return current
  
# Time Complexity
# Time: O(4^n) Space: O(4^n)

# Why O(4^n)?
# String length grows exponentially - roughly doubles every few iterations
# We do n iterations - each processing the current string
# Each iteration is linear in the current string length
# Combined effect: exponential growth × linear processing = exponential overall
# Simple explanation:
# Each step can make the string longer
# After many steps, strings get very long very fast
# Processing very long strings takes very long
# Result: exponential time complexity
# Bottom line: This algorithm gets extremely slow for large n (like n > 30) because the strings grow exponentially in length.

# The exact base (whether 2^n, 3^n, or 4^n) doesn't matter much - the key point is it's exponential, which means it becomes impractical for large inputs.