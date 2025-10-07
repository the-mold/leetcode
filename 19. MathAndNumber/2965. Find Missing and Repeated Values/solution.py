class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(int)
        repeating = -1

        rows = len(grid)
        cols = len(grid[0])

        # find repeating
        for r in range(rows):
            for c in range(cols):
                dic[grid[r][c]] += 1
                if dic[grid[r][c]] == 2:
                    repeating = grid[r][c]
        
        # find missing
        missing_number = -1
        sset = set(dic.keys())
        for i in range(1, len(sset) + 2):
            if i not in sset:
                missing_number = i
                break

        return [repeating, missing_number]