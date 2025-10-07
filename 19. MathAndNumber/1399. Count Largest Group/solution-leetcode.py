class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
      
# Time complexity: O(nlogn).
# The time complexity for calculating the sum of digits of x is O(log10x)=O(logx), so the total time required is O(nlogn). Selecting the maximum element and traversing the hash table both take O(n) time; therefore, the overall time complexity is O(nlogn)+O(n)=O(nlogn).

# Space complexity: O(logn).
# Using a hash map as auxiliary space, the number of digits of n is O(log10n)=O(logn), and each digit is in the range [0,9], so the hash map can contain at most O(10logn)=O(logn) keys, and the asymptotic space complexity is O(logn).