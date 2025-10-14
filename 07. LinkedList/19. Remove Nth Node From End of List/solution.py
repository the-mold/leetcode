def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Create a gap of n between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both until first hits the end
        while first:
            first = first.next
            second = second.next

        # Delete the target node
        second.next = second.next.next if second.next else None
        return dummy.next