# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def findMiddle(head):
  slow = head
  fast = head.next

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

#T:O(n)
#S:O(1)
