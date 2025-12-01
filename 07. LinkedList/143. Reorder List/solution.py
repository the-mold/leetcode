# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse second list
        l2_head = slow.next
        #break link between lists
        slow.next = None
        curr = l2_head
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # 3. zip two lists
        l1 = head
        tail = l1
        l2 = prev
        p1 = l1.next
        p2 = l2
        counter = 0

        while p1 and p2:
            if counter % 2 == 0:
                tail.next = p2
                p2 = p2.next
            else:
                tail.next = p1
                p1 = p1.next
            tail = tail.next
            counter += 1
        
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
        
        return l1

#T:O(n)
#S:O(1)
