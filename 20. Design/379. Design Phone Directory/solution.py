import collections

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.q = collections.deque([i for i in range(maxNumbers)])
        self.slots = [True] * maxNumbers

    def get(self) -> int:
        if not self.q:
            return -1

        slot_id = self.q.popleft()
        self.slots[slot_id] = False
        return slot_id

    def check(self, number: int) -> bool:
        return self.slots[number]
        
    def release(self, number: int) -> None:
        if self.slots[number]:
            return
        self.slots[number] = True
        self.q.append(number)
        


# Time complexity: O(1)
# In each get method call, we pop the first element from slotsAvailableQueue and mark it as not available in isSlotAvailable, both of which are constant time operations, thus each call will only take O(1) time.
# In each check method call, we only check if the value stored at the respective index in the isSlotAvailable array is true or not, thus each call will take O(1) time.
# In each release method call, we mark the value at the respective index in the isSlotAvailable array as true and push it in slotsAvailableQueue both of which are constant time operations, thus each call will take O(1) time.

# Space complexity: O(n)
# We use an additional queue slotsAvailableQueue and an array isSlotAvailable, both of which have a maximum size of n.
