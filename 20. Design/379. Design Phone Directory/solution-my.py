import heapq

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.capacity = maxNumbers
        self.slots = [i for  i in range(maxNumbers)]  #O(n)
        heapq.heapify(self.slots) #O(n)
        self.sset = set() #O(1)

    def get(self) -> int: # T:O(log n)
        if len(self.sset) == self.capacity:
            return -1
        
        slot_id = heapq.heappop(self.slots) #T:O(log n)
        self.sset.add(slot_id)
        return slot_id

    def check(self, number: int) -> bool: # T:O(1)
        return number not in self.sset

    def release(self, number: int) -> None:  # T:O(log n)
        if number not in self.sset:
            return

        self.sset.remove(number)
        heapq.heappush(self.slots, number)  # T:O(log n)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)