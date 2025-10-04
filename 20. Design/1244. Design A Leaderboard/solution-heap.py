
class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.board.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)

        res = 0
        while heap:
            res += heapq.heappop(heap)
        
        return res

    def reset(self, playerId: int) -> None:
        del self.board[playerId]
        

# Time Complexity:

# O(1) for addScore.
# O(1) for reset.
# O(K)+O(NlogK) = O(NlogK). It takes O(K) to construct the initial heap and then for the rest of the N−K elements, we perform the extractMin and add operations on the heap each of which take (logK) time.
# Space Complexity:

# O(N+K) where O(N) is used by the scores dictionary and O(K) is used by the heap.