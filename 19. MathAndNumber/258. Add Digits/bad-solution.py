class Solution:
    def addDigits(self, num: int) -> int:
        numberr = str(num)
        while len(numberr) != 1:
            local_sum = 0
            for i in numberr:
                local_sum += int(i)
            
            numberr = str(local_sum)
        
        return int(numberr)