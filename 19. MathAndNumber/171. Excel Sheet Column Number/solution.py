class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_number = 0
        for _, ch in enumerate(columnTitle):
            col_number = col_number * 26
            col_number += ord(ch) - ord("A") + 1
        
        return col_number

# For a title "LEET":
# L = 12
# E = (12 x 26) + 5 = 317
# E = (317 x 26) + 5 = 8247
# T = (8247 x 26) + 20 = 214442