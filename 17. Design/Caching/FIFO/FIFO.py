import collections
import threading

# FIFO - first in first out. When capacity is full, the first item to delete is the first(oldest) that came in.
class FIFO:
  def __init__(self, capacity):
    self.capacity = capacity
    self.dic = {}
    self.order = collections.deque()
    self._lock = threading.Lock()
    
  def get(self, key: str):
    with self._lock:
      self.dic.get(key, -1)
    
  def put(self, key, value):
    with self._lock:
      if key in self.dic:
        self.dic[key] = value
      else:
        self.dic[key] = value
        self.order.append(key)
        
        if self.capacity > len(self.order):
          key_to_deletet = self.order.popleft()
          del self.dic[key_to_deletet]
