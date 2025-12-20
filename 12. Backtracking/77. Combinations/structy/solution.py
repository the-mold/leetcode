def create_combinations(items, k):
  if len(items) < k:
    return []

  if k == 0:
    return [[]]

  first = items[0]

  partial_combos = create_combinations(items[1:], k-1)
  combos_with_first = []
  for comb in partial_combos:
    combos_with_first.append([first, *comb])

  combos_without_first = create_combinations(items[1:], k)

  return combos_with_first + combos_without_first