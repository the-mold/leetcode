# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            column_sum = l1_val +l2_val + carry
            carry = column_sum // 10
            newNode = ListNode(column_sum % 10)
            # link a new node to the new list starting at `dummyHead`
            current.next = newNode
            # move `current` pointer to the newly created node so that in next loops you could append new items to it.
            current = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyHead.next
    
# Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

# Space complexity : O(1). The length of the new list is at most max(m,n)+1 However, we don't count the answer as part of the space complexity.