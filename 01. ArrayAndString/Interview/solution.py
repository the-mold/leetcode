def count_max_3_palindromes(s):
  freq_map = collections.defaultdict(int)
  for ch in s:
    freq_map[ch] += 1
    
  num_pairs = 0
  num_singles = 0
  for ch in freq_map:
    num_pairs += freq_map[ch] // 2
    num_singles += freq_map[ch] % 2
    
  # Each palindrome needs 1 pair + 1 single
  return min(num_pairs, num_singles)

# T:O(n)
# S:O(n)  