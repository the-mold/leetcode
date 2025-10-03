class ListNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.freq = 1
    self.prev = None
    self.next = None

class DoubleLinkedList:
  def __init__(self):
    self.size = 0
    self.head = ListNode(-1,-1)
    self.tail = ListNode(-1,-1)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def add_to_tail(self, node):
    node.prev = self.tail.prev
    node.next = self.tail
    self.tail.prev.next = node
    self.tail.prev = node
    self.size += 1
  
  # remove least recently used node
  def remove_first_from_head(self):
    if self.size == 0:
      return
    node = self.head.next
    self.remove(node)
    return node
  
  def remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    self.size -= 1
  
  def is_empty(self):
    return self.size == 0

class LFU:
  def __init__(self, capacity):
    self.capacity = capacity
    self.key2node = {}
    self.freq_to_list = {}
    self.min_freq = 1
    
  def update_frequency(self, node):
      old_freq = node.freq
      
      # remove from old list
      old_list = self.freq_to_list[old_freq]
      old_list.remove(node)
      if old_freq == self.min_freq and old_list.is_empty():
        self.min_freq += 1
      
      new_freq = old_freq + 1
      node.freq = new_freq
      
      # append to the new freq2list
      if new_freq not in self.freq_to_list:
        self.freq_to_list[new_freq] = DoubleLinkedList()
      self.freq_to_list[new_freq].add_to_tail(node)
      
  def get(self, key):
    if key not in self.key2node:
      return -1
    
    node = self.key2node[key]
    self.update_frequency(node)
    return node.value
  
  def put(self, key, value):
    if self.capacity <= 0:
      return
    
    if key in self.key2node:
      node = self.key2node[key]
      node.value = value
      self.update_frequency(node)
    else:
      if len(self.key2node) >= self.capacity:
        # Remove LFU (and LRU among LFU) - remove from head
        min_freq_list = self.freq_to_list[self.min_freq]
        node = min_freq_list.remove_first_from_head()
        del self.key2node[node.key]
        
      node = ListNode(key, value)
      self.key2node[key] = node
      
      if 1 not in self.freq_to_list:
        self.freq_to_list[1] = DoubleLinkedList()
      self.freq_to_list[1].add_to_tail(node)
      self.min_freq = 1