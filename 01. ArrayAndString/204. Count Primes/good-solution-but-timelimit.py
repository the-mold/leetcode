class Solution:
    def countPrimes(self, n: int) -> int:
        # Count primes strictly less than n.
        if n < 3:
            return 0

        count = 0
        # Count primes strictly less than n.
        for i in range(2, n):
            if self.is_prime(i):
                count += 1
        
        return count

    def is_prime(self, num):
        if num < 2:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
        
        return True

#T:O(n√n)
#S:O(1)

countPrimes(2)
