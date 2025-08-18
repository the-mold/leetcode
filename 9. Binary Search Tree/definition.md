A Binary Search Tree (BST) is a special type of binary tree, which is a data structure where each node has at most two children: a left child and a right child.

What makes a BST special is its ordering property, which must be true for every single node in the tree.

Core Properties of a BST
For any given node (let's call it N):

Left Subtree Property: All values in N's left subtree must be less than N's value.
Right Subtree Property: All values in N's right subtree must be greater than N's value.
Recursive Property: Both the left and right subtrees of N must also be binary search trees themselves.
No Duplicates (Usually): By standard convention, BSTs do not contain duplicate values. If duplicates are allowed, they are typically all placed in the right subtree to maintain a consistent structure.

IMPORTANT!
Inoder tranverse goes through tree in a sorted manner.