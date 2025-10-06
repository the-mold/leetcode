class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(num):
            total_sum = 0
            while num:
                total_sum += (num % 10) ** 2
                num //= 10

            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
      
# Time complexity : O(243⋅3+logn+loglogn+logloglogn)... = O(logn).

# Finding the next value for a given number has a cost of O(logn) because we are processing each digit in the number, and the number of digits in a number is given by logn.

# To work out the total time complexity, we'll need to think carefully about how many numbers are in the chain, and how big they are.

# We determined above that once a number is below 243, it is impossible for it to go back up above 243. Therefore, based on our very shallow analysis we know for sure that once a number is below 243, it is impossible for it to take more than another 243 steps to terminate. Each of these numbers has at most 3 digits. With a little more analysis, we could replace the 243 with the length of the longest number chain below 243, however because the constant doesn't matter anyway, we won't worry about it.

# For an n above 243, we need to consider the cost of each number in the chain that is above 243. With a little math, we can show that in the worst case, these costs will be O(logn)+O(loglogn)+O(logloglogn).... Luckily for us, the O(logn) is the dominating part, and the others are all tiny in comparison (collectively, they add up to less than logn), so we can ignore them.

# Space complexity : O(logn).
# Closely related to the time complexity, and is a measure of what numbers we're putting in the HashSet, and how big they are. For a large enough n, the most space will be taken by n itself.

# We can optimize to O(243⋅3)=O(1) easily by only saving numbers in the set that are less than 243, as we have already shown that for numbers that are higher, it's impossible to get back to them anyway.