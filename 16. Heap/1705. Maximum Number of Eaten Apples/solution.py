class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        day = 0
        count = 0
        heap = []

        while day < len(apples) or heap:
            # 1. fill up the heap with new apples
            if day < len(apples) and days[day] > 0:
                expiration = day + days[day]
                heapq.heappush(heap, (expiration, apples[day]))

            # 2. cleanup heap
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # 3. eat an apple
            if heap:
                heap_days, heap_apples = heapq.heappop(heap)
                heap_apples -= 1
                count += 1
                if heap_apples > 0:
                    heapq.heappush(heap, (heap_days, heap_apples))
            
            day += 1
        
        return count

# T:O(nlogn), where logn is from heap operations
# S:O(n)