class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # go from left to right and eliminate closing gaps without a pair
        left_to_right_count = 0
        left_to_right_res = []
        for ch in s:
            if ch == "(":
                left_to_right_count += 1
                left_to_right_res.append(ch)
            elif ch == ")":
                if left_to_right_count > 0:
                    left_to_right_count -= 1
                    left_to_right_res.append(")")
            else:
                left_to_right_res.append(ch)

        # go from right to left and eliminate opening gaps without a pair
        right_to_left_count = 0
        right_to_left_res = []
        for i in range(len(left_to_right_res) - 1, -1, -1):
            ch = left_to_right_res[i]
            if ch == "(":
                if right_to_left_count > 0:
                    right_to_left_count -= 1
                    right_to_left_res.append(ch)
            elif ch == ")":
                right_to_left_count += 1
                right_to_left_res.append(ch)
            else:
                right_to_left_res.append(ch)

        return "".join(right_to_left_res[::-1])
      
# T:O(n)
# S:O(n)
