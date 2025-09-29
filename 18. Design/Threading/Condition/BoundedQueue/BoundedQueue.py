import threading
import collections

class BoundedQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.condition = threading.Condition()
    self.q = collections.deque()
    
  def get(self):
    with self.condition:
      while len(self.q) == 0:
        self.condition.wait()
      
      item = self.q.popleft()
      # let `put` method know that there is empty space now
      self.condition.notify()
      
      return item
    
  def put(self, item):
    with self.condition:
      while len(self.q) == self.capacity:
        self.condition.wait()
      
      self.q.append(item)
      print(f"Produced {item}")
      # Notify a waiting consumer that there's a new item
      self.condition.notify()
