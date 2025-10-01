class HitCounter:

    def __init__(self):
        self.dic = {}


    def hit(self, timestamp: int) -> None:
        self.dic[timestamp] = self.dic.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        start = 0 if timestamp <= 300 else timestamp - 300
        ans = 0
        for key, value in self.dic.items():
            if start < key <= timestamp:
                ans += value
        
        return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)