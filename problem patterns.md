# Two pointers
Used when going through a linnear structure(arr or linked list or strings).

Instead of brute force approach where you search the whole array for every element, two pointers approach improves it and reduces time complexity from n^2 to n.

Use case:
Pointers move in same dicrection. One is faster than the other one. Exampe: find middle of linked list.
Opposite direction. Example: find duplicates.


# Tree tranversal
Visit all nodes in tree exactly once.
Order of visiting has names:
Preorder tranversal(Data Left Right(DLR)): <root><all_children_on_the_left><all_children_on_the_right>
Inorder tranversal(LDR): <all_children_on_the_left><root><all_children_on_the_right>
Postorder tranversal(LRD): <all_children_on_the_left><all_children_on_the_right><root>

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

## Triggers----------------------

## Backtracking
- find all possible combinations of smth

## DP
- “longest”, “maximum”, “minimum”
- find optimal solution
What is the minimum cost of doing...
What is the maximum profit from...
How many ways are there to do...
What is number of ways you can do smth...
What is the longest possible...
Is it possible to reach a certain point...
Problems when you need to make decisions based on previous decisions 


## Binary search 
- sorted array
- You must write an algorithm with O(log n)

## Min Heap:
kth largest/smallest element


# When to use which algorith?

## Heap
When you need get-max, get-min with constant time O(1).
Push and pop take O(log n).

## BST
Search, insert, delete any key: O(log n).

## Simple binary tree
It is just tree with no ordering like in BST. Just use the BST.

## Linked lists
1. Insert/delete in the middle with O(1), without shifting neighbours(LRU cache with double linked list nodes).
2. Round-robin scheduling: Circular linked list for cyclic iteration.
