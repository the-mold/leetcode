# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, l1, l2):
        dummyHead = ListNode(0)
        current = dummyHead
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                newNode = ListNode(l1.val)
                current.next = newNode
                current = newNode
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                current.next = newNode
                current = newNode
                l2 = l2.next

        if l1 != None:
            current.next = l1
        if l2 != None:
            current.next = l2
        
        return dummyHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        stack = lists.copy()

        while stack and len(stack) != 1:
            l1 = stack.pop()
            l2 = stack.pop()

            l_sorted = self.merge2Lists(l1, l2)
            stack.append(l_sorted)
        
        return stack[0]

#Intuition:
# write a method to merge two lists and loop all over k lists.

# Time complexity : O(kN) where k is the number of linked lists.
# We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.

# Space complexity : O(1)
# We can merge two sorted linked list in O(1) space.