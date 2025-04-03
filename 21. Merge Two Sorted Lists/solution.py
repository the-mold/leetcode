# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):   
    root = ListNode()
    current = root

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    # append if one of lists is not exhausted
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    

    return root.next

def print_linked_list(l):
    node = l
    while node:
        print("->", node.val)
        node = node.next
            
    print("done printing")



# T: O(n+m), where n and m and lengthes of lists 
# M: O(1), because no additional structures created. You just rearranged pointers.  


# TEST=====
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

merged_head = mergeTwoLists(l1, l2)

# Print the merged list
print_linked_list(merged_head)