class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                num = stack.pop()
                if num == 0:
                    stack[-1] += 1
                else: 
                    stack[-1] += 2 * num
        
        return stack[0]
      
# T:O(n)
# S:O(n)
