def find_max_number(x: int, y: int, n: int) -> str:
  larger = max(x, y)
  smaller = min(x, y)

  # edge case to avoid division by 0
  if smaller == 0:
    # if smaller elem is 0, then solution is only possible if n us divisible by larger number
    if n % larger == 0:
      return str(larger) * (n // larger)
    else:
      return str(0)

  larger_count = n // larger
  while larger_count >= 0:
    remainder = n - larger_count * larger

    if remainder % smaller == 0:
      smaller_count = remainder // smaller
      return str(larger) * larger_count + str(smaller) * smaller_count 

    larger_count -= 1
  
  return str(0)
