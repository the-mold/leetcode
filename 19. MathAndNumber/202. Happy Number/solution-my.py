class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()
        local_sum = 0
        while num != 0:
            local_sum += (num % 10) ** 2
            num //= 10

            if num == 0:
                if local_sum == 1:
                    return True
                if local_sum in seen:
                    return False
                
                seen.add(local_sum)
                num = local_sum
                local_sum = 0
        
        return False

# Time Complexity: O(log n)
# Cost of Summing Digits: For a number k, the number of digits is approximately log10(k). The inner part of your while loop runs once for each digit. So, calculating the sum of squares for a number k takes O(log k) time.
# Size of the Numbers: Let's analyze how large the numbers in the sequence can get.
# The largest possible sum of squares for a 3-digit number is for 999, which is 9² + 9² + 9² = 243.
# The largest possible sum for a 4-digit number is for 9999, which is 4 * 81 = 324.
# Even for a very large number like 9,999,999,999,999 (13 digits), the sum is only 13 * 81 = 1053.
# This shows that any number with 4 or more digits will quickly shrink to a number with 3 or fewer digits. The maximum sum for a number under 1000 is 999 -> 243. The maximum sum for a number under 243 is 199 -> 1² + 9² + 9² = 163.
# Cycle Detection: After the first step, all subsequent numbers in the sequence are relatively small (bounded by a constant, around 243). The number of steps until a cycle is detected or 1 is reached is therefore also bounded by a constant. Because the set of numbers to check is finite and small, you will find a cycle or 1 in a constant number of steps.
# Conclusion: The first step takes O(log n) time to process the initial input n. All subsequent steps take a constant amount of time because the numbers are small. Therefore, the overall time complexity is dominated by the first step, making it O(log n).

# Space Complexity: O(log n)
# The seen Set: The space complexity is determined by the maximum number of items you store in the seen set before finding a cycle or reaching 1.
# Size of Elements in the Set: As established above, the numbers generated in the sequence after the first step are bounded by a small constant. The largest number you'd likely store is the first sum calculated from the input n.
# Maximum Value: The maximum value of this first sum is proportional to the number of digits in n, which is log n. For an input n with d digits, the maximum sum is d * 81. For example, for n = 999, the first sum is 243.