import time
import threading

class Bucket:
  def __init__(self, capacity, refill_rate):
    self.capacity = capacity
    self.refill_rate = refill_rate
    self.tokens = capacity
    self.time = time.monotonic
    self.time_last_refill = time.monotonic()
  
  def refill(self):
    current_time = self.time()
    # Note: time.monotonic returns a floating point number so time_since_last_refill could be 1.5
    time_since_last_refill = current_time - self.time_last_refill # 
    
    # tokens to add since last refill 
    new_tokens = time_since_last_refill * self.refill_rate
    
    self.tokens = min(self.capacity, self.tokens + new_tokens)
    self.time_last_refill = current_time
    

class TokenBucketRateLimiter:
  def __init__(self, capacity, refill_rate):
    self.capacity = capacity
    self.refill_rate = refill_rate
    self._buckets = {}
    self._lock = threading.Lock()
  
  def allow(self, key:str):
    with self._lock:
      if key not in self._buckets:
        self._buckets[key] = Bucket(self.capacity, self.refill_rate)
      
      bucket = self._buckets[key]
      
      # 1. Refill the bucket with any new tokens that have accrued.
      bucket.refill()
      
      # 2. Check if there is at least one token to spend.
      if bucket.tokens >= 1:
        # 3. If so, consume one token and allow the request.
        bucket.tokens -= 1
        return True
      
      return False
