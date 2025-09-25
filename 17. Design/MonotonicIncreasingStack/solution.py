class MonotonicIncreasingStack:
  """
    A stack that maintains elements in a monotonically increasing order.
    When a new element is pushed, any elements at the top of the stack
    that are larger than the new element are popped.
    """
  def __init__(self):
    self.stack = []
    
  def push(self, value:int):
    """
    Pushes a value onto the stack, maintaining the monotonic property.

    Pops elements from the top of the stack until the top element is
    less than or equal to the value being pushed.
    """
    while self.stack and self.stack[-1] > value:
      self.stack.pop()
    self.stack.append(value)
    
  def pop(self):
    if self.stack:
      return self.stack.pop()
    
  def peek(self):
    if self.stack:
      return self.stack[-1]
  
# Explanation of the Demonstration:
# Push 3: Stack is [3].
# Push 1: 3 > 1, so 3 is popped. Then 1 is pushed. Stack is [1].
# Push 4: 1 <= 4. Stack is [1, 4].
# Push 2: 4 > 2, so 4 is popped. 1 <= 2. Then 2 is pushed. Stack is [1, 2].
# Push 5: 2 <= 5. Stack is [1, 2, 5].