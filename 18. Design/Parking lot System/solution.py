import json

class Car:
  def __init__(self, license_plate):
    self.license_plate = license_plate
  
  def get_license_plate(self):
    return self.license_plate
    
class ParkingLotSystem:
  def __init__(self, capacity):
    self.capacity = capacity
    self.slot_to_car = {}
    self.car_to_slot = {}
  
  def checkin(self, car: Car):
    slot_id = self.get_first_free_slot()
    if slot_id >= 0:
      car_id = car.get_license_plate()
      self.slot_to_car[slot_id] = car_id
      self.car_to_slot[car_id] = slot_id
    else:
      print("no free slots")
  
  def checkout(self, car: Car):
    car_id = car.get_license_plate()
    if car_id not in self.car_to_slot:
      raise Exception(f"unknown car id: {car_id}")

    slot_id = self.car_to_slot[car_id]
    del self.car_to_slot[car_id]
    del self.slot_to_car[slot_id]
  
  def stats(self):
    slots_free = self.capacity - len(self.slot_to_car)
    return json.dumps({
      "slots_free": slots_free,
    })

  def get_first_free_slot(self):
    for i in range(self.capacity):
      if i not in self.slot_to_car:
        return i
    return -1

if __name__ == "__main__":
  ps = ParkingLotSystem(100)
  
  c1 = Car("B1111")
  c2 = Car("B2222")
  c3 = Car("B3333")
  
  ps.checkin(c1)
  ps.checkin(c2)
  print(ps.stats())
  ps.checkin(c3)
  print(ps.stats())
  ps.checkout(c3)
  ps.checkout(c1)
  print(ps.stats())
