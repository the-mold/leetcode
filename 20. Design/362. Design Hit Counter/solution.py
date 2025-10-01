from collections import deque

class HitCounter:

    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()

        return len(self.q)