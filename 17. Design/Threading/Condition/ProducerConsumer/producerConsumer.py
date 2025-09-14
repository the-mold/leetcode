import threading
import time

condition = threading.Condition()
items = []

def producer():
  for i in range(5):
    with condition:
      items.append(i)
      # Wake up one waiting consumer thread
      condition.notify()
    time.sleep(0.5)
      
def consumer():
  while True:
    with condition:
      if not items:
        condition.wait()
        
      item = items.pop()
      print(f"got item in consumer: {item}")
    

thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
