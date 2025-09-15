import threading
import time

event = threading.Event()

def worker(idx):
  print(f"worker {idx}. Ready to do job")
  event.wait()
  print(f"worker {idx}. doing job \n")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]

for t in threads:
  t.start()

print("\n---------\n")
event.set()

for t in threads:
  t.join()
