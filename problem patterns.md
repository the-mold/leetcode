# Two pointers
Used when going through a linnear structure(arr or linked list or strings).

Instead of brute force approach where you search the whole array for every element, two pointers approach improves it and reduces time complexity from n^2 to n.

Use case:
Pointers move in same dicrection. One is faster than the other one. Exampe: find middle of linked list.
Opposite direction. Example: find duplicates.


# Binary search
It requires a sorted array!!! Here you divide steps by 2 to achieve T:O(log n).

# Breadth-first search
Going through tree level-by-leve from top to bottom. Uses a queue.
It is the best for searching the shortest path or reporting tree by levels.

# Depth-first search
You go deep in one route to explore all nodes before you explore other nodes. Uses a call stack(recursion).
It is the best used for exploring all paths in the tree.


# Priority queue
Use it every time problem says "Find Kth largest/smallest elements in array", "Top K elements", "K closest elements to origin". 

# Dynamic problem
Breaking down a complex problem into set of simpler underlying propblems AND reusing result of those undelying problems to solve the original problem.
## Approaches
Top-down: TODO.
Bbottom-up: More efficient: Example: CoinChange, Break strings in words from dict.



<!-- 
Reverse the second half of a linked list​
Find all anagrams in a string​
Merge overlapping intervals -->




Pattern	              Example Problems	                            Key Technique
Sliding Window	      Max consecutive ones, longest substring	      Dynamic window, 2 pointers
Two Pointers	        Reverse string, sorted array two sum	        Left/right indexes
Prefix Sum	          Subarray sum equals k	                        Running sum + hash map
Binary Search	        Search in rotated array, kth smallest element	Custom condition mid-search
Backtracking	        N-Queens, combinations	                      Recursion with pruning
DFS/BFS	              Number of islands, word ladder	              Queue or recursion
Dynamic Programming	  Climbing stairs, longest palindrome	          DP table or memoization
Monotonic Stack/Queue	Daily temperatures, sliding window max	      Stack/queue that maintains order
Union Find (DSU)	    Connected components, redundant connection	  Disjoint Set with path compression
Greedy	              Jump game, interval scheduling	              Make best local choice

## Triggers
If you see...	                          It’s probably...
“longest”, “maximum”, “minimum”	        Sliding Window or DP
“contiguous subarray”	                  Prefix Sum or Sliding Window
“sorted array”	                        Two Pointers or Binary Search
“all combinations/permutations”	        Backtracking
“shortest path”	                        BFS or Dijkstra
“number of islands”, “regions”	        DFS/BFS or Union Find
“can you reach”, “can you finish”	      DFS cycle detection
“intervals”, “merge”	                  Sorting + Greedy or Heap