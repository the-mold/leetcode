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
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        def helper(l, r):
            if l > r:
                return
        
            mid = (l+r) // 2
            root = TreeNode(nums[mid])

            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)

            return root

        return helper(0, len(nums) - 1)
        