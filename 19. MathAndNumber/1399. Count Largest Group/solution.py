import collections

class Solution:
    def _digit_sum(self, n):
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digit_sum
    
    def countLargestGroup(self, n: int) -> int:
        dic = collections.defaultdict(list)

        for i in range(1, n + 1):
            dic[self._digit_sum(i)].append(i)
        
        max_group_size = max(len(v) for v in dic.values())

        count = 0
        for v in dic.values():
            if len(v) == max_group_size:
                count += 1

        return count
      