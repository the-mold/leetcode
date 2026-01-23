Given a binary tree where each node contains a value, analyze the 'islands'—maximal connected components of nodes that share the same value. Your task is to count how many such islands exist, how large they are, and how different value-based regions form across the tree. Islands are determined strictly by parent–child connectivity.

Input:

nodes = [1, 1, 0, 1, 1, null, 0]
Output:

2 islands total: 1 island of value 1, 1 island of value 0

Explanation: Tree structure:

      1
     / \
    1   0
   / \   \
  1   1   0
All 1s are connected through parent–child links, forming a single island of value 1 (size 4). The two 0s are connected to each other and form a single island of value 0 (size 2). Therefore, the tree has 2 islands total.

Constraints:

The number of nodes in the tree is in the range [0, 10^4]
Node values are typically 0 or 1, but can be any integer
An island is a maximal connected component of nodes with the same value
Two nodes are connected if they have a parent–child relationship