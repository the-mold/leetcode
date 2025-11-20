class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
        # Initialze numbers[2] through numbers[n-1] as True because we assume each number
        # is prime until we find a prime number (p) that is a divisor of the number
        numbers = [False, False] + [True] * (n - 2)
        
        # math.floor(math.sqrt(n)) + 1 is the last element we need to check when we search for the prime for a number. 
        # Any number larger than `math.floor(math.sqrt(n)) + 1` does not need to be checked. 
        for p in range(2, math.floor(math.sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        # numbers[index] will only be true where index is a prime number
        # return the number of indices whose value is true.
        return sum(numbers)
    
# T:O(n * sqrt(n))
# S:O(1)