def comprehension(nums):
  res = []
  for idx, num in enumerate(nums):
    if idx % 2 == 0 and num % 2 == 0:
      res.append(num)
  return res


print("test", comprehension([ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ])) #[10, 18, 78]