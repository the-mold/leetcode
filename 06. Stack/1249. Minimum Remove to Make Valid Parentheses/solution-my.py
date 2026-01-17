class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = collections.deque()

        res = []
        for idx, ch in enumerate(s):
            if ch == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((")", idx))
            elif ch == "(":
                stack.append(("(", idx))
        
        res = []
        to_remove = None
        if stack:
            to_remove = stack.popleft()
        for idx, ch in enumerate(s):
            if to_remove and ch == to_remove[0] and idx == to_remove[1]:
                if stack:
                    to_remove = stack.popleft()
                else: 
                    to_remove = None
            else:
                res.append(ch)
        
        return "".join(res)

# T:O(n)
# S:O(n)
