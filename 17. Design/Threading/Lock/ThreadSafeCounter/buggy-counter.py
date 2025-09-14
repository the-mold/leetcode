import time
import threading

class InsecureCounter:
  def __init__(self):
    self.value = 0

def insecure_counter(counterClass, times):
  for i in range(times):
    current_value = counterClass.value
    time.sleep(0.0001)    
    counterClass.value = current_value + 1
    
counter_unsafe = InsecureCounter()
threads = [threading.Thread(target=insecure_counter, args=(counter_unsafe, 1000)) for _ in range(2)]
print(f"threads: {len(threads)}")
for t in threads:
  t.start()
for t in threads:
  t.join()
  
print(f"result {counter_unsafe.value}")
