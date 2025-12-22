import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current_smallerst_number = 1
        self.add_back_heap = []
        self.add_back_set = set()
        

    def popSmallest(self) -> int:
        # first check if there is smth to return from add_back_heap
        if self.add_back_heap:
            res = heapq.heappop(self.add_back_heap) #O(log k)
            self.add_back_set.remove(res)
            return res
        else:
            #otherwise return from current_smallerst_number
            res = self.current_smallerst_number
            self.current_smallerst_number += 1
            return res
        

    def addBack(self, num: int) -> None:
        # number is already in the set
        if num >= self.current_smallerst_number:
            return

        if num not in self.add_back_set:
            heapq.heappush(self.add_back_heap, num) #O(log k)
            self.add_back_set.add(num)
        

#T:O(log k), where k is number of items in heap
#S:O(k)