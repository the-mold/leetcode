def permutations(items):
  if len(items) == 0:
    return [[]]

  first = items[0]
  full_permutations = []
  for perm in permutations(items[1:]):
    for i in range(len(perm) + 1): #+1 because you want to also append element in the end
      full_permutations.append(perm[:i] + [first]  + perm[i:])

  return full_permutations

# n = length of elements array
# Time: ~O(n!)
# Space: ~O(n!)