class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        previx_dict = collections.defaultdict(int)
        previx_dict[0] = 1

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k
            if remainder in previx_dict:
                res += previx_dict[remainder]

            previx_dict[remainder] += 1
        
        return res