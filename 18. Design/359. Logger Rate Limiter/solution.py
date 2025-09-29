import threading

class Logger:

    def __init__(self):
        self.dic = {} # [message]: timestamp
        self._lock = threading.Lock()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        with self._lock:
            if message not in self.dic:
                self.dic[message] = timestamp
                return True

            last_message_time = self.dic.get(message)
            if timestamp - last_message_time < 10:
                return False
            
            self.dic[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)