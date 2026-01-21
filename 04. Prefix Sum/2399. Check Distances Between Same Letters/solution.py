class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen_idx = [None] * 26

        for idx, ch in enumerate(s):
            ch_code = ord(ch) - ord("a")
            if seen_idx[ch_code] == None:
                 seen_idx[ch_code] = idx
            else:
                if (idx - seen_idx[ch_code] - 1) != distance[ch_code]:
                    return False
        
        return True

#T:O(n)
#S:O(n)
