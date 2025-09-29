class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            _, prev_min = self.stack[-1]
            self.stack.append((val, min(prev_min, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Intuition
# Store a tuple in stack (value, current_min_value). In this way, you always have access to the min value.


# Time Complexity : O(1) for all operations.
# push(...): Checking the top of a Stack, comparing numbers, and pushing to the top of a Stack (or adding to the end of an Array or List) are all O(1) operations. Therefore, this overall is an O(1) operation.
# pop(...): Popping from a Stack (or removing from the end of an Array, or List) is an O(1) operation.
# top(...): Looking at the top of a Stack is an O(1) operation.
# getMin(...): Same as above. This operation is O(1) because we do not need to compare values to find it. If we had not kept track of it on the Stack, and instead had to search for it each time, the overall time complexity would have been O(n).

# Space Complexity : O(n).
# Worst case is that all the operations are push. In this case, there will be O(2⋅n)=O(n) space used.
