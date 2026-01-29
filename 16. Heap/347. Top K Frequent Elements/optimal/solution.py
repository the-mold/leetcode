class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1

        freq_bucket = [[] for _ in range((len(nums) + 1))]
        for key in d:
            count = d[key]
            freq_bucket[count].append(key)
 
        # loop backwords because you are intereseted in highest counts
        res = []
        for i in range(len(freq_bucket) - 1, -1, -1):
            if len(freq_bucket[i]) == 0:
                continue
            for j in range(len(freq_bucket[i])):
                res.append(freq_bucket[i][j])
                if len(res) == k:
                    return res
        
        return []

# T:O(n)
# S:O(n)


# Why the nested loop is still T:O(n):
# The key insight is that across all iterations of the outer loop, the inner loop runs at most n times total, not n² times.
# Each number from nums appears in exactly one bucket
# The inner loop processes each number exactly once
# Total elements processed = n
# Think of it this way: you're visiting each of the n elements once, just organized by buckets.
# Total: O(n) + O(n) + O(n) = O(n)