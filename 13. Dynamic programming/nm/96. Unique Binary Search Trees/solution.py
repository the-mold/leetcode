class Solution:
    def numTrees(self, n: int) -> int:
        return self._numTrees(1, n, {})

    def _numTrees(self, start, end, memo):
        key = (start, end)
        if key in memo:
            return memo[key]

        # The base case if start > end: return 1 represents an empty subtree, and there's exactly 1 way to construct an empty subtree (which is to have no nodes at all). This happens when you try to construct an empty tree.
        # Example: root = 1 in range [1,3]
        #left_count = countTrees(1, 0)  # start=1, end=0 → start > end
        # This means "left subtree of root 1 has no nodes"
        # There's exactly 1 way to have no nodes: empty tree
        if start > end:
            return 1

        total = 0
        for i in range(start, end+1):
            left = self._numTrees(start, i-1, memo)
            right = self._numTrees(i+1, end, memo)
            # multiply left by right to get combination
            total += left * right
        
        memo[key] = total
        return memo[key]

# Time: O(nm)
# Space: O(nm)
