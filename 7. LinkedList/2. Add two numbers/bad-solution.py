# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def resolveLinkedListvalue(self, llist, value: str):
        newValue = f"{llist.val}{value}"
        if llist.next:
            return self.resolveLinkedListvalue(llist.next, newValue)
        return newValue

    def createNode(self, parent, array):
        if len(array) == 0:
            return
        
        parent.next = ListNode(array[0])
        
        self.createNode(parent.next, array[1:])

    def createLList(self, array):
        array.reverse()
        root = ListNode(array[0])
        self.createNode(root, array[1:])
        return root

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.resolveLinkedListvalue(l1, "")
        n2 = self.resolveLinkedListvalue(l2, "")
        sum = int(n1) + int(n2)
        res = []
        for digit in str(sum):
            res.append(int(digit))
        
        return self.createLList(res)

    