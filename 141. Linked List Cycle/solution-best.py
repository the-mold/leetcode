# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle(head):
  slow = fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.slow.slow

    if slow == fast:          #if there is a loop, then pointers will eventually be the same. If they are the same, then there is a loop.
      return True

  return False

#T:O(n)
#S:O(1)           #solution has a better space complexity
