#Note! this approach is confusing. Try the other one with linkedList.

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_frequency = 0
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        # update freq
        old_freq = self.key2freq[key]
        self.key2freq[key] = old_freq + 1

        self.freq2key[old_freq].pop(key)
        if not self.freq2key[old_freq]:
            del self.freq2key[old_freq]

        self.freq2key[old_freq + 1][key] = 1
        if self.min_frequency not in self.freq2key:
            self.min_frequency += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.key2val:
            self.get(key) # reuse get logic from above to update frequency
            self.key2val[key] = value
            return
        
        if len(self.key2val) == self.capacity:
            delkey, _ = self.freq2key[self.min_frequency].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.min_frequency = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)