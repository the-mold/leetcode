class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Explanation. Let's say that k is 2.
        # self.getNumberOfSubarrayLessThanKWithingTheWindow(nums, k) include all subarrays count of size 1, 2.
        # self.getNumberOfSubarrayLessThanKWithingTheWindow(nums, k - 1) will count all subarrays of size 1.
        # To get answer of arrays of ONLY size 2, substruct the first from the second. See Venn diagram explanation.
        return self.getNumberOfSubarrayLessThanKWithingTheWindow(nums, k) - self.getNumberOfSubarrayLessThanKWithingTheWindow(nums, k - 1)

    def getNumberOfSubarrayLessThanKWithingTheWindow(self, nums, k):
        freq_map = collections.defaultdict(int)

        l = 0
        count = 0

        for r in range(len(nums)):
            freq_map[nums[r]] += 1
            
            # move left pointer
            while len(freq_map) > k:
                freq_map[nums[l]] -= 1
                if freq_map[nums[l]] == 0:
                    del freq_map[nums[l]]
                l += 1

            # total number of subarrays that a window can form
            count += r - l + 1

        return count


# T:O(n)
# S:O(n)
