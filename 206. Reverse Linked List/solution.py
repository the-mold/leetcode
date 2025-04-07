# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # Save the next node
            next_node = current.next

            # Reverse the link so that current_node.next points to the node before it
            current.next = prev
            prev = current

            # Move to the next node in the original list
            current = next_node

        return prev
    
#T: O(n)
#S: O(1)