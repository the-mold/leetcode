# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            # after each intteration start from the beginning to find where to insert the new node
            prev = dummy

            # find the position to insert the new node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # save the next element to be itterated 
            temp = curr.next
            # insert new element
            curr.next = prev.next
            prev.next = curr

            # reassign the next element to be itterated
            curr = temp
        
        return dummy.next