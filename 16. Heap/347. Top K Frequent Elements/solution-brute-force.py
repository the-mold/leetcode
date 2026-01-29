class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1

        res = [(key, d[key]) for key in d]
        res.sort(key=lambda x:x[1], reverse=True)
        return res[:k]

# T:O(nlogn)
# S:O(n)

