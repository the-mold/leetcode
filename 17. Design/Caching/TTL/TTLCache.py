import threading
import time

class TTLCache:
  """
  A Time-To-Live (TTL) Cache implementation.

  This cache evicts items after a specified time-to-live has passed.
  Expiration is checked passively on each 'get' operation.
  """
  
  def __init__(self, capacity, ttl):
    if capacity <= 0 or not isinstance(capacity, int):
      raise ValueError("invalid capacity")
    
    self.capacity = capacity
    self.default_ttl = ttl
    self._time = time.monotonic
    self._cache = {}
    self._lock = threading.Lock()
    
    # cleanup
    self.cleanup_interval = 300
    self._stop_event = threading.Event()
    self._cleanup_job = threading.Thread(
      target=self._cleanup_runner
    )
    self._cleanup_job.start()
  
  def _cleanup_runner(self):
    while not self._stop_event.wait(self.cleanup_interval):
      self._cleanup()
  
  def _cleanup(self):
    with self._lock:
      self._cache = {
        key: value 
        for key, value in self._cache.items()
        if value[0] < self._time()
      }
  
  def stop(self):
    self._stop_event.set()
    self._cleanup_job.join()
  
  def put(self, key, value, ttl=None):
    with self._lock:
      ttl = ttl if ttl is not None else self.default_ttl
      if ttl <= 0:
        # if ttl is 0, then just remove the chached entry and return
        if key in self._cache:
          del self._cache[key]
        return
      
      expiration = self._time() + ttl
      self._cache[key] = (value, expiration)

  def get(self, key):
    """
    Retrieves an item from the cache.

    If the item is found, it checks for expiration. If the item has
    expired, it's removed from the cache and None is returned.

    :param key: The key of the item to retrieve.
    :return: The value of the item, or None if the key is not found
              or the item has expired.
    """
    with self._lock:
      if key not in self._cache:
        return -1
      
      value, expiration = self._cache[key]
      
      # check if time is expired
      if self._time() > expiration:
        del self._cache[key]
        return -1
    
      return value
  