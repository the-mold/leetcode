# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle(head):
  current = head
  visited = set()

  while current:
    if current in visited:
      return True
    
    visited.add(current)
    current = current.next

  return False

#T:O(n)
#S:O(n)
