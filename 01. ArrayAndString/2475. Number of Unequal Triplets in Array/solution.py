# Intuition: count combinations of frequencies rather than all individual combinations.

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        distinct = list(freq.keys())

        count = 0
        for i in range(len(distinct)):
            for j in range(i + 1, len(distinct)):
                for k in range(j+1, len(distinct)):
                    v1 = freq[distinct[i]]
                    v2 = freq[distinct[j]]
                    v3 = freq[distinct[k]]
                    count += v1 * v2 * v3
        return count
      
# Time Complexity: O(n + d³) Building the frequency map takes O(n) time. Then we iterate through all combinations of 3 distinct values, which is O(d³) where d is the number of distinct values (at most 100). Since d ≤ 100 and is typically much smaller than n, this is very efficient
# Space Complexity: O(d) The frequency map stores at most d distinct values, where d ≤ min(n, 100). In practice, this is much smaller than n