class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next

# Intuition
# 1. Traverse all the linked lists and collect the values of the nodes into an array.
# 2. Sort and iterate over this array to get the proper value of nodes.
# 3. Create a new sorted linked list and extend it with the new nodes.


# Time complexity : O(NlogN) where N is the total number of nodes.

# Collecting all the values costs O(N) time.
# A stable sorting algorithm costs O(NlogN) time.
# Iterating for creating the linked list costs O(N) time.
# Space complexity : O(N).

# Sorting cost O(N) space (depends on the algorithm you choose).
# Creating a new linked list costs O(N) space.