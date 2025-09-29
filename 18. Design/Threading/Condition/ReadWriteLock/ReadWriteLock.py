import threading
import time
import random

class ReadWriteLock:
  def __init__(self):
    self.condition = threading.Condition()
    self.write_active = False
    self.writers_waiting = 0
    self.readers_count = 0
    
  def acquire_read(self):
    with self.condition:
      while self.write_active or self.writers_waiting > 0:
        self.condition.wait()
      
      self.readers_count += 1
      
  def release_read(self):
    with self.condition:
      self.readers_count -= 1
      if self.readers_count == 0:
        self.condition.notify_all()
        
  def acquire_write(self):
    with self.condition:
      self.writers_waiting += 1
      while self.readers_count > 0 or self.write_active:
        self.condition.wait()
      
      self.writers_waiting -= 1
      self.write_active = True
  
  def release_write(self):
    with self.condition:
      self.write_active = False
      self.condition.notify_all()
     
     
     
# Example
config = {"version": 1.0, "author": "Cascade"}
lock = ReadWriteLock()

def reader_thread(thread_id):
    for i in range(5):
        print(f"[Reader {thread_id}] Attempting to read...")
        lock.acquire_read()
        try:
            print(f"[Reader {thread_id}] Reading config: Version is {config['version']}. (Active readers: {lock.readers_count})")
            time.sleep(random.uniform(0.1, 0.3)) # Simulate reading time
        finally:
            print(f"[Reader {thread_id}] Finished reading.")
            lock.release_read()
        time.sleep(random.uniform(0.5, 1))

def writer_thread():
    for i in range(2):
        time.sleep(random.uniform(1, 2)) # Writer works less frequently
        print("\n[Writer] ==> Attempting to write...")
        lock.acquire_write()
        try:
            print("[Writer] ==> Acquired write lock. Updating config...")
            new_version = config["version"] + 0.1
            config["version"] = round(new_version, 2)
            time.sleep(0.5) # Simulate writing time
            print(f"[Writer] ==> Config updated to version {config['version']}.\n")
        finally:
            lock.release_write()

if __name__ == "__main__":
    readers = [threading.Thread(target=reader_thread, args=(i,)) for i in range(3)]
    writer = threading.Thread(target=writer_thread)

    writer.start()
    for r in readers:
        r.start()

    for r in readers:
        r.join()
    writer.join()

    print("\nFinal Config:", config)