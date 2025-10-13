class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        level = 1
        coins_on_level_left = level
        for i in range(n):
            coins_on_level_left -= 1
            if coins_on_level_left == 0:
                level += 1
                coins_on_level_left = level
        
        return level if coins_on_level_left == 0 else level - 1

#T:O(1)
#S:O(1)