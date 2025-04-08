def countPrimes(n):
    ans = 0
    for i in range(2, n + 1):
        if is_prime(i):
            ans += 1
    
    return ans

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


#T:O(n√n)
#S:O(1)

countPrimes(2)
