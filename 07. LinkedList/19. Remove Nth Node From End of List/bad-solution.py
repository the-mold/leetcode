# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        list_length = 0
        while node:
            list_length += 1
            node = node.next

        if list_length < 2:
            return None
        if list_length < n:
            return head
        node = head
        prev = None
        node_idx_to_remove = list_length - n
        if node_idx_to_remove == 0:
            return head.next
        for _ in range(node_idx_to_remove):
            prev = node
            node = node.next
        prev.next = node.next

        return head