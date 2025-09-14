import threading
import time

class SafeCounter:
  def __init__(self):
    self.value = 0
    self.lock = threading.Lock()
    
def safe_counter_increment(counterInstnce, times):
  for i in range(times):
    with counterInstnce.lock:
      current_value = counterInstnce.value
      time.sleep(0.0001)
      counterInstnce.value = current_value + 1

sc = SafeCounter()
threads = [threading.Thread(target=safe_counter_increment, args=(sc, 1000)) for _ in range(2)]

for t in threads:
  t.start()
for t in threads:
  t.join()
  
print(f"result: {sc.value}")
