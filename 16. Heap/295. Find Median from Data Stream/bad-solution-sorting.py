class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def _is_even(self):
        return len(self.arr) & 1 == 0

    def findMedian(self) -> float:

        # must sort every time
        self.arr.sort()
        
        n = len(self.arr)
        if n == 0:
            return 0
        if n == 1:
            return self.arr[0]

        if self._is_even():
            start = n // 2 - 1
            end = start + 1
            return (self.arr[start] + self.arr[end]) / 2
        else:
            return self.arr[math.ceil(n / 2 - 1)]


#T:O(nlogn)