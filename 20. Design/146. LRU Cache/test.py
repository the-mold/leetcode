class ListNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None
    
class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.dic = {}
    self.head = ListNode(-1,-1)
    self.tail = ListNode(-1,-1)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def _remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
  
  def _add(self, node):
    self.tail.prev.next = node
    node.prev = self.tail.prev
    node.next = self.tail
    self.tail.prev = node
  
  def get(self, key):
    if not key in self.dic:
      return -1
    
    node = self.dic[key]
    self._remove(node)
    self._add(node)
    
    return node.value
  
  def put(self, key, value):
    node = self.dic.get(key)
    if node:
      self._remove(node)
    
    node = ListNode(key, value)
    self._add(node)
    self.dic[key] = node 
    
    if len(self.dic) > self.capacity:
      least_used_node = self.head.next
      self._remove(least_used_node)
      del self.dic[least_used_node.key]
