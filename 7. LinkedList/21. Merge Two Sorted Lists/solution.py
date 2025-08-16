# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyList = ListNode(0)
        current = dummyList

        while list1 != None and list2 != None:
            l1_val = list1.val
            l2_val = list2.val

            if l1_val >= l2_val:
                newNode = ListNode(l2_val)
                current.next = newNode
                current = newNode
                list2 = list2.next if list2 else None
            else:
                newNode = ListNode(l1_val)
                current.next = newNode
                current = newNode
                list1 = list1.next if list1 else None
        
        # add remaining items from list1
        if list1 != None:
            current.next = list1

        # add remaining items from list2
        if list2 != None:
            current.next = list2

        return dummyList.next

# Time complexity : O(n+m)
# Because exactly one of l1 and l2 is incremented on each loop
# iteration, the while loop runs for a number of iterations equal to the
# sum of the lengths of the two lists. All other work is constant, so the
# overall complexity is linear.

# Space complexity : O(1)
# The iterative approach only allocates a few pointers, so it has a
# constant overall memory footprint.
