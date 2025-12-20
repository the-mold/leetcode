class MedianFinder:

    def __init__(self):
        self.arr = []

    def _find_idx_to_insert(self, num):
        # binary search
        l = 0
        r = len(self.arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if num == self.arr[mid]:
                return mid
            elif num > self.arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return l

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            idx_to_insert = self._find_idx_to_insert(num) # O(log n)
            self.arr.insert(idx_to_insert, num) # O(n)

    def _is_even(self):
        return (len(self.arr) & 1) == 0

    def findMedian(self) -> float:
        n = len(self.arr)
        if self._is_even():
            start = (n // 2) - 1
            end = start + 1
            return (self.arr[start] + self.arr[end]) / 2
        else:
            median_idx = math.ceil(len(self.arr) / 2) - 1
            return self.arr[median_idx]


# T:
  #addNum: O(n) because of insert operation
  # findMedian: O(1)
# S: O(n)
