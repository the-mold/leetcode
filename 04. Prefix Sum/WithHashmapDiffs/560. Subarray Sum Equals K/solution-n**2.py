class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)
        
        count = 0
        for a in range(len(prefix)):
            for b in range(a + 1, len(prefix)):
                if b - a == k:
                    count += 1

        return count 

# T:O(n**2)
# S:O(N)
