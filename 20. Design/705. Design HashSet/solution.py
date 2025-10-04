class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.buckets = [Bucket() for _ in range(self.key_range)]
        
    def _get_hash_key(self, key:int):
        return key % self.key_range

    def add(self, key: int) -> None:
        hash_key = self._get_hash_key(key)
        self.buckets[hash_key].add(key)

    def remove(self, key: int) -> None:
        hash_key = self._get_hash_key(key)
        self.buckets[hash_key].remove(key)
        
    def contains(self, key: int) -> bool:
        hash_key = self._get_hash_key(key)
        return self.buckets[hash_key].exists(key)

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class Bucket:
    def __init__(self):
        self.head = ListNode(-1)

    def exists(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next
        return False
    
    def add(self, key):
        if not self.exists(key):
            new_node = ListNode(key)
            new_node.next = self.head.next
            self.head.next = new_node
    
    def remove(self, key):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)