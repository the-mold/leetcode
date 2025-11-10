class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event1[0] <= event2[0]:
            return event1[1] >= event2[0]
        else:
            return event2[1] >= event1[0]

# T:O(1)
# S:O(1)
