
class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.board.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.board[playerId]
        

# Time Complexity:

# O(1) for addScore.
# O(1) for reset.
# O(NlogN) for top where N represents the total number of players since we sort all of the player scores and then take the top K from the sorted list.
# Space Complexity:

# O(N) used by the scores dictionary and also by the new list formed using the dictionary values in the top function.