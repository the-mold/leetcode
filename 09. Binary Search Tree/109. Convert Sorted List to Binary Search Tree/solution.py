# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            # Important! return when list hast only one node
            if not node.next:
                return TreeNode(node.val)
            
            slow = fast = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            # slow is my mid
            root = TreeNode(slow.val)

            # split the list in half so that .left and .right recursions could work.
            if prev:
                prev.next = None

            root.left = helper(node)
            root.right = helper(slow.next)

            return root

        return helper(head)

