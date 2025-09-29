import heapq

class ParkingLotSystem:
  def __init__(self, capacity):
    self._free = list(range(capacity))
    heapq.heapify(self._free)
    self.car_to_slot = {}
    
  def enter(self, car_id):
    slot_id = heapq.heappop(self._free)
    self.car_to_slot[car_id] = slot_id
    return slot_id
  
  def leave(self, car_id):
    slot_id = self.car_to_slot[car_id]
    del self.car_to_slot[car_id]
    heapq.heappush(self._free, slot_id)
    return slot_id
  