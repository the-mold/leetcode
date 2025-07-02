def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
  if n == 0:
      return True

  pointer = 0
  l1 = len(flowerbed)

  def valid(k):
      if flowerbed[k] == 1:
          return False
      # previous item
      if k > 0 and flowerbed[k - 1] == 1:
          return False
      if k + 1 < l1 and flowerbed[k + 1] == 1:
          return False
      
      return True

  while pointer < len(flowerbed):
      if valid(pointer):
          n -= 1
          # no more flowers left, you can return
          if n == 0:
              return True
          
          flowerbed[pointer] = 1

      pointer += 1
  
  # no more flowers left
  return n == 0 

#T:O(n)
#S:O(1)


canPlaceFlowers([1,0,0,0,1], 1) #True
canPlaceFlowers([1,0,0,0,1], 2) #Flase