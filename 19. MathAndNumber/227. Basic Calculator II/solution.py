class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_number = 0
        # sign of the first operation is "+"
        operation = "+"
        for idx, ch in enumerate(s):
            if ch.isnumeric():
                curr_number = (curr_number * 10) + int(ch)
            # must be a separate if stament because it is called for the last charachter
            if (not ch.isnumeric() and ch != " ") or idx == (len(s) - 1):
                if operation == "+":
                    stack.append(curr_number)
                elif operation == "-":
                    stack.append(-curr_number)
                elif operation == "*":
                    stack.append(stack.pop() * curr_number)
                elif operation == "/":
                    # do `int(stack.pop() / curr_number)` instead of `stack.pop() // curr_number`
                    # because dividing negative charachters is tricky and might result in unexpected output
                    stack.append(int(stack.pop() / curr_number))
                
                # update current operation
                operation = ch
                curr_number = 0

        res = 0
        while stack:
            res += stack.pop()

        return res

#T:O(n)
#S:O(n)
