class BrowserHistory:
    def __init__(self, homepage: str):
        self._history, self._future = [], []
        # 'homepage' is the first visited URL.
        self._current = homepage

    def visit(self, url: str) -> None:
        # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self._history.append(self._current)
        self._current = url
        # We need to delete all entries from 'future' stack.
        self._future = []

    def back(self, steps: int) -> str:
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current

    def forward(self, steps: int) -> str:
        # Pop elements from 'future' stack, and push elements in 'history' stack.
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current
      
      
# Time complexity:

# In the visit(url) method, we push the URL string in the history stack, assign the given url string as the current URL, and then we clear the future stack, all these operations take O(1) time each.
# Thus, in the worst case each call to the visit(url) method will take O(1) time.

# In the back(steps) and forward(steps) methods, we push and pop strings in the future and history stacks. We do these two operations unless we are done with m steps or all elements are removed from the stack which might have n elements in it.
# Thus, in the worst case, each call to these methods will take O(min(m,n)) time.

# Space complexity:

# We might visit n URL strings and they will be stored in our stacks.
# Thus, in the worse case, we use O(l⋅n) space.