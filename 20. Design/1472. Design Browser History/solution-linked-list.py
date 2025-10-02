class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.root = ListNode(homepage)
        self.current_node = self.root

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.current_node.next = new_node
        new_node.prev = self.current_node
        self.current_node = new_node

    def back(self, steps: int) -> str:
        step_count = steps
        while self.current_node.prev and step_count:
            self.current_node = self.current_node.prev
            step_count -= 1
        return self.current_node.value

    def forward(self, steps: int) -> str:
        step_count = steps
        while self.current_node.next and step_count:
            self.current_node = self.current_node.next
            step_count -= 1
        return self.current_node.value 
        

# Time complexity:

# In the visit(url) method, we insert a new node in our doubly linked list, it will take O(l) time to create a new node (to allocate memory for l characters of the url string), and then we mark this new node as current which will take O(1) time.
# Thus, in the worst case each call to the visit(url) method will take O(l) time.

# In the back(steps) and forward(steps) methods, we iterate on our doubly linked list nodes and stop when m nodes are iterated or we reached the end.
# Thus, in the worst case, each call to these methods will take O(min(m,n)) time.

# Space complexity:

# We might visit n URL strings and they will be stored in our doubly linked list.
# Thus, in the worse case, we use O(l⋅n) space.