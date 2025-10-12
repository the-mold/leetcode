class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ""

        for ch in s:
            if ch.isnumeric():
                current_number = 10 * current_number + int(ch)
            elif ch == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif ch == "]":
                prev_string, number = stack.pop()
                current_string = prev_string + number * current_string
            else:
                current_string += ch
        
        return current_string

#T:O(n)
#S:O(1)
