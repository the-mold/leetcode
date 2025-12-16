class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res == res[::-1]

# T:O(n)
# S:O(n)
