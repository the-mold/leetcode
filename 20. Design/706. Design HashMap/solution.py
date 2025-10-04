class MyHashMap:
    def __init__(self):
        self.capacity = 2069
        self.hashmap = [[] for _ in range(self.capacity)]
        
    def get_index(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.get_index(key)

        # check if item exists
        for idx, item in enumerate(self.hashmap[index]):
            if key == item[0]:
                self.hashmap[index][idx] = (key, value)
                return
        
        # otherwise add a new item
        self.hashmap[index].append((key, value))

    def get(self, key: int) -> int:
        index = self.get_index(key)
        for idx, item in enumerate(self.hashmap[index]):
            if key == item[0]:
                return item[1]
        
        return -1

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        for idx, item in enumerate(self.hashmap[index]):
            if key == item[0]:
                del self.hashmap[index][idx]


# Time Complexity: for each of the methods, the time complexity is O( K/N​) where N is the number of all possible keys and K is the number of predefined buckets in the hashmap, which is 2069 in our case.
# In the ideal case, the keys are evenly distributed in all buckets. As a result, on average, we could consider the size of the bucket is  
# K/N.

# Since in the worst case we need to iterate through a bucket to find the desire value, the time complexity of each method is O(K/N).

# Space Complexity: O(K+M) where K is the number of predefined buckets in the hashmap and M is the number of unique keys that have been inserted into the hashmap.
