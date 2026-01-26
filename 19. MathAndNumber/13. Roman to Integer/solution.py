roman_map = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}

def romanToInt(s: str) -> int:
  total = 0
  n = len(s)
  for i in range(n):
    current_value = roman_map[s[i]]
    next_idx = i + 1

    # check if next value is more then current
    if next_idx < n and current_value < roman_map[s[next_idx]]:
      # substract current_value from total
      total -= current_value
    else:
      # add current_value to total
      total += current_value

  return total


# T:O(n)
# S:O(1)

romanToInt("MCMXCIV")
