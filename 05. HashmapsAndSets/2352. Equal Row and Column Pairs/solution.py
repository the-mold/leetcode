#Note! Use tuples for rows and cols because tuples are hashable(can be a key to a dictionary).
#It makes lookups much fater.

def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)

    # 1. make map of rows
    rows_map = {}
    for i in range(n):
        row_key = tuple(grid[i])
        rows_map[row_key] = rows_map.get(row_key, 0) + 1

    # 2. for each column make a tuple and check if it exists in rows_map
    count = 0
    for i in range(n):
        col_arr = []
        for j in range(len(grid[0])):
            col_arr.append(grid[j][i])
        col_key = tuple(col_arr)

        count += rows_map.get(col_key, 0)

    return count

#T:O(n^2)
#S:O(n^2) - one tuple takes O(n). In worst case you create a tuple for each row AND each column.
