class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        rooms_available = list(range(n))
        rooms_occupied = []

        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # free up rooms if you can
            while rooms_occupied and rooms_occupied[0][0] <= start:
                _, room_id = heapq.heappop(rooms_occupied)
                heapq.heappush(rooms_available, room_id)

            if rooms_available:
                room_id = heapq.heappop(rooms_available)
                heapq.heappush(rooms_occupied, (end, room_id))
                count[room_id] += 1
            else:
                # all are occupied. Pop one from occupied
                end, room_id = heapq.heappop(rooms_occupied)
                # the new end time of the meeting is end of the previous + own duration
                heapq.heappush(rooms_occupied, (end + duration, room_id))
                count[room_id] += 1
        
        return count.index(max(count))

# T:O(nlogn + MlogM)
# S:O(n)