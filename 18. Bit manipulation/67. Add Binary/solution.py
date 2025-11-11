class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        p1 = len(a) - 1
        p2 = len(b) - 1

        while carry or p1 >= 0 or p2 >= 0:
            p1_val = int(a[p1]) if p1 >= 0 else 0
            p2_val = int(b[p2]) if p2 >= 0 else 0
            
            curr_sum = carry + p1_val + p2_val

            # if curr_sum 3, append 1
            # if curr_sum 2, append 0
            # if curr_sum 1, append 1
            # if curr_sum 0, append 0
            res.append(curr_sum % 2)
            # if curr_sum 3, carry is 1
            # if curr_sum 2, carry is 1
            # if curr_sum 1, carry is 0
            # if curr_sum 0, carry is 0
            carry = curr_sum // 2

            p1 -= 1
            p2 -= 1
        
        res.reverse()
        # map is for mapping each int to str
        return "".join(map(str, res))

# T:O(n + m)
# S:O(1)