class Solution:

    def __init__(self, w: List[int]):
        self.items = []
        for idx, value in enumerate(w):
            for _ in range(value):
                self.items.append(idx)
        

    def pickIndex(self) -> int:
        return random.choice(self.items)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()