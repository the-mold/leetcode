class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = []
        odd = []

        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort()
        odd.sort(reverse=True)

        even_idx = 0
        odd_idx = 0
        res = [0] * n

        for i in range(n):
            if i % 2 == 0:
                res[i] = even[even_idx]
                even_idx += 1
            else:
                res[i] = odd[odd_idx]
                odd_idx += 1
        
        return res

#T:O(n)
#S:O(n)