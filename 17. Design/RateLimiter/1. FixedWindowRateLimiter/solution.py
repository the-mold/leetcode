import time
import threading


class FixedWindowRateLimiter:
  def __init__(self, capacity: int, window_seconds: int):
    if not isinstance(capacity, int) or capacity <= 0:
      raise ValueError("invalid capacity")
    if not isinstance(window_seconds, int) or window_seconds <= 0:
      raise ValueError("invalid window seconds")
    
    self.capacity = capacity
    self.window_seconds = window_seconds
    self._time = time.monotonic
    self._buckets = {}
    self._lock = threading.Lock()
    
    self._stop_event = threading.Event()
    self._cleanup_interval = 60 * 5 # 5 min
    self._cleanup_task = threading.Thread(
      target=self._background_cleanup_task, # need to start this task with while loop, otherwise the _cleanup task will run once and quit.
      name="CleanupThread",
      # daemon=True # to be able to quite the process
    )
    self._cleanup_task.start()
  
  def allow(self, user_id: str) -> bool:
    with self._lock:
      window = self._buckets.get(user_id)
      current_time = self._time()
      if not window:
        self._buckets[user_id] = (current_time, 1)
        return True
        
      window_start_time, count = window
      
      # reset new time frame
      if current_time > window_start_time + self.window_seconds:
        self._buckets[user_id] = (current_time, 1)
        return True
    
      # increment time
      if count < self.capacity:
        self._buckets[user_id] = (window_start_time, count + 1)
        return True
      else:
        return False

  def _background_cleanup_task(self):
    """
    This loop will run until the _stop_event is set.
    The .wait(timeout) method returns True if the event was set,
    so the loop breaks.
    """
    while not self._stop_event.wait(self._cleanup_interval):
      self._cleanup()
    print("Cleanup thread finished.")

  def _cleanup(self):
    with self._lock:
      current_time = self._time()
      
      # rebuild the bucket. Cannot `del` certain keys in loop in python
      self._buckets = {
        key: value 
        for key, value in self._buckets.items()
        if current_time - value[0] > self.window_seconds       
      }
  
  def stop(self):
    """A public method to gracefully shut down the background thread."""
    print("Signaling cleanup thread to stop...")
    # 2. Set the event to signal the while loop to exit.
    self._stop_event.set()
    
    # 3. Use .join() to wait for the thread to finish its last task.
    self._cleanup_job.join()
    print("Cleanup thread has been joined.")
  