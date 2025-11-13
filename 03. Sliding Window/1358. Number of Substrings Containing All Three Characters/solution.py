class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        freq_map = collections.defaultdict(int)

        for r, ch in enumerate(s):
            freq_map[ch] += 1

            while len(freq_map) == 3:
                # all substrings that start at l and end with r and beyond are valid!
                # Example: "abcaa". 
                # When l = 0 and r = 2, valid are: ["abc", "abca", "abcaa"] = 3 OR len(s) - r 
                count += len(s) - r 

                freq_map[s[l]] -= 1
                if freq_map[s[l]] == 0:
                    del freq_map[s[l]]
                l += 1
            
            r += 1
        
        return count

# T:O(n)
# S:O(n)
