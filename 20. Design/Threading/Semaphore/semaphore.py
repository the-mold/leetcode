import threading
import time

semaphore = threading.Semaphore(3)

def worker(idx: int):
  with semaphore:
    # do some work
    print(f"doing work for worker: {idx}") 
    time.sleep(1)
    
threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]

for t in threads:
  t.start()
for t in threads:
  t.join()
