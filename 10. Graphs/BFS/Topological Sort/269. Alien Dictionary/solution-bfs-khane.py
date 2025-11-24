class Solution:
    def alienOrder(self, words: list[str]) -> str:
      n = 0
      adj_map = collections.defaultdict(set)
      
      # construct indegree object
      indegree = collections.defaultdict(int)
      all_letters = set("".join(words))
      for letter in all_letters:
        indegree[letter] = 0
        
      # construct adj_map.
      # All words in input are sorted. You need to find first letter that differs between two words. It means that letter in w1 comes before w2.
      for i in range(n-1): #loop over all words excep the last one, because we have nothing to compare it agains.
        w1 = words[i]
        w2 = words[i+1]
        
        min_length = min(len(w1), len(w2))
        
        # edge case: longer word comes before shorter. This violates the problem condition.
        #Invalid order if a longer word comes before its prefix (e.g., ["abc", "ab"])
        if len(w1) > len(w2) and w1.startswith(w2):
          # solution is impossible, according to the problem statement
          return ""
        
        # find the first letter that differs
        for j in range(min_length):
          if w1[j] != w2[j]:
            # we found a new graph relationship: w1[j] -> w2[h]. 
            # Add it to adj_map if it is not known.
            if w1[j] not in adj_map[w2[j]]:
              # w2[j] depends on w1[j]
              adj_map[w2[j]].add(w1[j])
              indegree[w2[j]] += 1

            break #important! compare only the first char that differs
              
        # Khane's algorithm      
              
        # contruct initial state of q. Visit nodes with no indegree dependencies
        q = collections.deque()
        for key, val in indegree.items():
          if val == 0:
            q.append(key)
        
        res = []
            
        while q:
          visited_node = q.popleft()
          res.append(visited_node)
          
          for neighbor in adj_map[visited_node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
              q.append(neighbor)
              
        if len(res) < len(all_letters):
          # no solution possible
          return ""
        else:
          return "".join(res)
        
# Key Variables
# N: The number of words in the input list (len(words)).
# C: The total number of characters across all words in the input list.
# U: The number of unique characters in the alphabet. This is the number of vertices in our graph. U is at most C.
# Time Complexity: O(C)
# The overall time complexity is dominated by the total number of characters in all words, C. Here's the breakdown of each step:

# Graph Initialization (O(C)):
# all_chars = set("".join(words)): This line first joins all words into a single string of length C, which takes O(C) time. Then, it creates a set from that string, which also takes O(C) time.
# The loop for char in all_chars: runs U times, which is insignificant compared to C.
# Complexity for this step: O(C)
# Rule Extraction / Graph Building (O(C)):
# The outer loop for i in range(len(words) - 1): runs N-1 times.
# Inside, the inner loop for j in range(min_len): compares characters of adjacent words.
# The total number of character comparisons across all pairs of words is, at most, the sum of the lengths of all words. This is because we only iterate up to the length of the shorter word in each pair.
# Therefore, the total work done in this section is proportional to the total number of characters, C.
# Complexity for this step: O(C)
# Kahn's Algorithm (Topological Sort) (O(U + E) which simplifies to O(U²) or O(C)):
# The standard complexity for Kahn's algorithm is O(V + E), where V is the number of vertices and E is the number of edges.
# In our graph:
# V (vertices) = U (unique characters).
# E (edges) = The number of unique precedence rules. In the worst case, every character could have a rule connecting it to every other character, so E could be up to O(U²).
# The while queue: loop processes each character (vertex) and each rule (edge) exactly once.
# The line for neighbor in sorted(list(adj[char])): adds a small overhead. Sorting the neighbors of a character char takes O(k log k) where k is the number of neighbors. Summed over all characters, this is bounded but adds to the complexity. However, since U is small (at most 26 for English alphabet, or limited by problem constraints), this is often negligible.
# Since U <= C and E is also related to C, the complexity of this step is bounded by O(C).
# Complexity for this step: O(U + E), which is effectively bounded by O(C).
# Overall Time Complexity: O(C) + O(C) + O(C) = O(C).

# Space Complexity: O(U) or O(1)
# The space complexity depends on the size of the alphabet, U.

# adj (Adjacency List):
# Stores the graph. In the worst case, it can have U keys, and the sets of values can contain up to U-1 neighbors each. This leads to O(U²). However, the number of edges E is at most N-1 or U², whichever is smaller. A tighter bound is O(U + E).
# in_degree (In-degree Map):
# Stores the in-degree for each of the U unique characters.
# Space: O(U)
# all_chars (Set):
# Stores all U unique characters.
# Space: O(U)
# queue (Deque):
# In the worst case, all U characters could have an in-degree of 0 and be in the queue simultaneously.
# Space: O(U)
# result (List):
# Stores the final sorted alphabet of U characters.
# Space: O(U)
# Overall Space Complexity: The dominant factor is the storage for the graph structures, which is proportional to the number of unique characters U. So, the space complexity is O(U).

# If the problem guarantees a fixed-size alphabet (like the 26 lowercase English letters), the space complexity can be considered O(1), as U would be a constant.
        