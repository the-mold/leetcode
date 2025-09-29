"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    visited = {}

    def getOrCreateNode(self, node):
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]
        else:
            newNode = Node(node.val, None, None)
            self.visited[node] = newNode
            return newNode

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        original_head = head

        while head != None:
            newNode = self.getOrCreateNode(head)
            newNode.next = self.getOrCreateNode(head.next)
            newNode.random = self.getOrCreateNode(head.random)

            head = head.next if head else None
        
        return self.visited[original_head]
    
# T:O(n)
# S:O(n), because of dictionary to store visited nodes

#Intuition
# I go though every node in the old list. For each node I try:
# 1. for node itself: create or get a clone from visited object
# 2. for newNode.next: create or get a clone from visited object
# 3. for newNode.random: create or get a clone from visited object

# For every node you either link known nodes, or you create and assign new nodes. The newly created nodes must be memorized in visited object.
