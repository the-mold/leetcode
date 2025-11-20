class Solution:
    def countPrimes(self, n: int) -> int:
        # Count primes strictly less than n.
        if n < 3:
            return 0

        count = 0
        # Count primes strictly less than n.
        for i in range(2, n): #O(n)
            if self.is_prime(i):
                count += 1
        
        return count

    # Note: you can find prime like this but it is not optimal
    def is_prime(self, num):
        if num < 2:
            return False

        for i in range(2, num): # O(n)
            if num % i == 0:
                return False
        
        return True

#T:O(n**2)
#S:O(1)

countPrimes(2)
