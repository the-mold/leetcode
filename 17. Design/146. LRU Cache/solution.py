class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        # Note! no need to make changes in self.dic becuase i just move element to the end of the list.
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # remove if node with key existed, since we need to move it to the end anyway
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.add(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            # assigning node_to_delete is a MUST, because ref to it is lost after self.remove()
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

        

# Time complexity: O(1) for both get and put.

# For get:
# Check if a key is in a hash map. This costs O(1).
# Get a node associated with a key. This costs O(1).
# Call remove and add. Both methods cost O(1).
# For put:

# Check if a key is in a hash map. This costs O(1).
# If it is, we get a node associated with a key and call remove. Both cost O(1).
# Create a new node and insert it into the hash map. This costs O(1).
# Call add. This method costs O(1).
# If the capacity is exceeded, we call remove and delete from the hash map. Both cost O(1).
# Space complexity: O(capacity)

# We use extra space for the hash map and for our linked list. Both cannot exceed a size of capacity.