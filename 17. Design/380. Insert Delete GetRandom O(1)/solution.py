import collections
import random

class RandomizedSet:

    def __init__(self):
        self.order = collections.deque()
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.order.append(val)
        self.dic[val] = len(self.order) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        idx = self.dic[val]
        last_element = self.order[-1]
        # overwrite element that you want to delete with the last element. Then you can just pop the last element in array with O(1)
        self.order[idx] = last_element
        self.dic[last_element] = idx

        self.order.pop()
        del self.dic[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.order)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()