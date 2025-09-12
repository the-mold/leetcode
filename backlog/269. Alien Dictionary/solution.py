class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        Finds the order of characters using a DFS-based topological sort.
        """
        # Step 1: Initialize data structures using standard Python objects
        adj = {char: set() for char in "".join(words)}

        # Step 2: Build the graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        # Step 3: Perform DFS-based topological sort
        # visited: nodes that have been fully processed (post-order)
        # visiting: nodes currently in the recursion stack (for cycle detection)
        visited = {}
        result = []

        # We need a list of all unique characters to iterate over
        all_chars = list(adj.keys())

        def dfs(char):
            """Performs DFS and returns True if no cycle is detected, False otherwise."""
            visited[char] = 'visiting' # Mark as currently in recursion stack

            # sorted() provides a deterministic order
            for neighbor in sorted(list(adj[char])):
                if neighbor in visited:
                    # If the neighbor is in the current recursion stack, we have a cycle
                    if visited[neighbor] == 'visiting':
                        return False
                else:
                    # If the recursive call finds a cycle, propagate the failure
                    if not dfs(neighbor):
                        return False
            
            visited[char] = 'visited' # Mark as fully processed
            result.append(char)
            return True

        # Iterate through all characters to handle disconnected components
        for char in all_chars:
            if char not in visited:
                if not dfs(char):
                    return "" # Cycle detected

        # The result is the reverse of the post-order traversal
        return "".join(reversed(result))

# --- Complexity Analysis ---

# Let C be the total number of characters in all words combined.
# Let U be the number of unique characters (the size of the alphabet).
# Let N be the number of words in the input list.
# Let E be the number of edges (rules), where E <= N-1.

# Time Complexity: O(C)
# 1. Building the graph: O(C), as we iterate through all characters to find rules.
# 2. DFS traversal: We visit each character (node) and each rule (edge) exactly once. This is O(U + E). 
# Since C is the dominant factor (C >= U and C >= N > E), the total time complexity is O(C).

# Space Complexity: O(U + E) or O(U + N)
# 1. `adj` (adjacency list): Stores U characters and E edges. O(U + E).
# 2. `visited` (state tracking): Stores a state for each of the U characters. O(U).
# 3. Recursion stack: In the worst case (a long chain of dependencies), the stack depth can be U. O(U).
# The total space is dominated by the adjacency list and recursion stack, making it O(U + E).



# --- Intuition ---
# 1. Build the Graph: We create an adjacency list representing the character dependencies.
# 2. DFS Traversal: We'll perform a DFS from each unvisited character. During the traversal, we need to keep track of three states for each character (node) to detect cycles:
# Unvisited: The node has not been processed yet.
# Visiting: The node is currently in our recursion stack. If we encounter a "visiting" node, we've found a cycle.
# Visited: The node and all its descendants have been fully processed.
# 3. Generate Order: The topological order is the reverse of the post-order traversal from the DFS. We'll add each character to our result list only after we have visited all its neighbors.
