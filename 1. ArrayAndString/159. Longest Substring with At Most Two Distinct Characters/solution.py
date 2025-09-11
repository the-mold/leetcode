class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        hashmap = {}
        l, r = 0, 0

        max_length = 0
        while r < len(s):
            # save index
            hashmap[s[r]] = r 

            if len(hashmap) == 3:
                min_idx = min(hashmap.values())
                del hashmap[s[min_idx]]
                l = min_idx + 1
          
            max_length = max(max_length, r - l + 1)
            r += 1
        
        return max_length

# T:O(n)
# S:O(1), there is a hashmap but its size is limited to 3, hence constat space