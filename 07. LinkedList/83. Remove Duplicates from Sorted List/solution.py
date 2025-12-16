class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            if prev is not None and curr.val == prev.val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return head

# T:O(n)
# S:O(1)