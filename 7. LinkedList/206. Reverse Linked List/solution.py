# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
    
#T: O(n)
#S: O(1)

# Intuition
# You move through very node in list and change .next pointer to the previous node. Note:
# 1. You need to keep track of the previous node.
# 2. You need to save ref to the next node temporarily before you overwrite the .next with prev reference. Otherwise, you will not know what is the next node.
