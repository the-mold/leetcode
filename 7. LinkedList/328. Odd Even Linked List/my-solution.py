# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: #cases [], [1], [1,1]. No need to change them
            return head

        idx_full = 1
        tail = head
        while tail.next:
            tail = tail.next
            idx_full += 1

        original_tail = tail  # Remember where the original list ends
        idx = 1 
        curr_node = head  
        prev = None

        while curr_node and idx <= idx_full:
            # save original next because you might lose access to it if you modify pointers. You overwrite it in `tail.next = None`
            next_node = curr_node.next

            if idx % 2 == 0:
                # assign odd node to the end
                tail.next = curr_node
                tail = tail.next
                tail.next = None #break the cycle

                # reassign previous to skip the current node
                if prev:
                    prev.next = next_node
            else:
                # previous is reassigned only if it changes: only when current node is odd
                prev = curr_node
            
            curr_node = next_node
                
            idx += 1
        
        return head

#T: O(n)
#S: O(1)