#Intuition:
# for every char i colors, compare it with the next char. If char


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    # eliminate the left baloon
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
                    # no need to increment r. r is incremented by the main loop
            else:
                l = r
                # no need to increment r. r is incremented by the main loop
        
        return res