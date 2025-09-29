class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head

    return head
  