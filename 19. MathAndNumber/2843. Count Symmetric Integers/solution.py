class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if self.is_symmetric(i):
                count += 1
        
        return count
    
    def is_symmetric(self, i):
        s = str(i)

        if len(s) % 2 != 0:
            # odd numbers are never symmetric
            return False
        
        mid = len(s) // 2
        start = s[:mid]
        end = s[mid:]

        start = sum(int(digit) for digit in start)
        end = sum(int(digit) for digit in end)

        return start == end
