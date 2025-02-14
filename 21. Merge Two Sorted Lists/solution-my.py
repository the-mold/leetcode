# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = flattenList(list1, []) or []
        l2 = flattenList(list2, []) or []

        expected_list_length = len(l1) + len(l2)

        print("l1", l1)
        print("l2", l2)

        loop_over_idx = 0
        check_list_idx = 0
        loop_over_list = l1
        check_list = l2
        if len(l2) > len(l1):
            loop_over_list = l2
            check_list = l1

          

        res = []
        while len(res)< expected_list_length:
            if loop_over_idx >= len(loop_over_list) and check_list_idx >= len(check_list):
                break
            
            # take only from first list  
            elif loop_over_idx <= len(loop_over_list) and check_list_idx >= len(check_list):
                print("only 1 is given")
                res.append(loop_over_list[loop_over_idx])
                loop_over_idx += 1
            # take only from second list  
            elif loop_over_idx >= len(loop_over_list) and check_list_idx <= len(check_list):
                print("only 2 is given")

                res.append(check_list[check_list_idx])
                check_list_idx += 1    
            # compare numbers
            else:
                if loop_over_list[loop_over_idx] >= check_list[check_list_idx]:
                    print("1 is greater")
                    print("1 is ", loop_over_list[loop_over_idx], type(loop_over_list[loop_over_idx]))
                    print("2 is ", check_list[check_list_idx])
                    res.append(loop_over_list[loop_over_idx])
                    loop_over_idx += 1
                else:
                    print("2 is greater")
                    res.append(check_list[check_list_idx])
                    check_list_idx += 1 


        print("res", res)
        # return joinLinkedLists(l1, l2)


def flattenList(l, res):
    if not l:
        return l

    res.append(l.val)
    if l.next:
        flattenList(l.next, res)
    
    return res

