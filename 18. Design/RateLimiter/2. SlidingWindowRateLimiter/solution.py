import time
import threading

class SlidingWindowRateLimiter:
  def __init__(self, capacity, window_seconds):
    self.capacity = capacity
    self.window_seconds = window_seconds
    self._time = time.monotonic
    self._buckets = {}
    self._lock = threading.Lock()
    
    self._stop_event = threading.Event()
    self._cleanup_interval = 60 * 5 # 5 Min 
    self._cleanup_job = threading.Thread(
      target=self._run_cleanup_job,
      name="cleanupJob",
      # daemon=True.  <- not needed when i use _stop_event
    )
    self._cleanup_job.start()
  
  def _run_cleanup_job(self):
    while not self._stop_event.wait(self._cleanup_interval):
      self._cleanup()
  
  def _cleanup(self):
    current_time = self._time()
    
    with self._lock:
      # Rebuild the dictionary, keeping only buckets that have seen
      # activity within the last window period.
      self._buckets = {
        key: timestamps
        for key, timestamps in self._buckets.items()
        # A bucket is stale if its last request is older than the window.
        # This check ensures we don't remove recently active users.
        if timestamps and timestamps[-1] > (current_time - self.window_seconds)
      }
  
  def allow(self, key: str) -> bool:
    current_time = self._time()

    with self._lock:
      if key not in self._buckets:
        self._buckets[key] = []
      
      timestamps = self._buckets.get(key)    
      window_start = current_time - self.window_seconds
      
      # remove all timestamps that are older then the window start
      while timestamps and timestamps[0] < window_start:
        timestamps.pop(0)
      
      if len(timestamps) < self.capacity:
        timestamps.append(current_time)
        return True

      return False
    
  def stop(self):
    """A public method to gracefully shut down the background thread."""
    print("Signaling cleanup thread to stop...")
    # 2. Set the event to signal the while loop to exit.
    self._stop_event.set()
    
    # 3. Use .join() to wait for the thread to finish its last task.
    self._cleanup_job.join()
    print("Cleanup thread has been joined.")
    

  
if __name__ == "__main__":
  rt = SlidingWindowRateLimiter(10, 30)
  rt.allow("user-1")
  