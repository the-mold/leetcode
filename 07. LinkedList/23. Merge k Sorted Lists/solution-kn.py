# Intuition: merge lists one by one as if it is merge 2 lists problem.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])

        return res

# T:O(kN)
# S:O(1), because you just reuse the nodes, you do not not create new ones. If you would create nodes with ListNode(val), the space would be O(n).
