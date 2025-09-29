import time
import threading

class SlidingWindow:
  def __init__(self, capacity, window_seconds):
    self.capacity = capacity
    self.window_seconds = window_seconds
    self._time = time.monotonic
    self._buckets = {}
    self._lock = threading.Lock()
    
    self._stop_event = threading.Event()
    self._cleanup_task = threading.Thread(target=self.cleanup)
    self._cleanup_task.start()
    
  def stop(self):
    self._stop_event.set()
    self._cleanup_task.join()
  
  def _cleanup_runner(self):
    while not self._stop_event.wait(5 * 60):
      self.cleanup()
    
  def cleanup(self):
    curr_time = self._time()
    with self._lock:
      self._buckets = {
        k: v 
        for k, v in self._buckets
        if curr_time - v[-1] > self.window_seconds
      }
    
  def allow(self, key: str):
    curr_time = self._time()
    
    with self._lock:
      if not key in self._buckets:
        self._buckets[key] = []
        
      window_times = self._buckets[key]
      window_start = curr_time - self.window_seconds
      while window_times and window_times[0] < window_start:
        window_times.pop(0)
        
      if len(window_times) < self.capacity:
        window_times.append(curr_time)
        return True
      else:
        return False