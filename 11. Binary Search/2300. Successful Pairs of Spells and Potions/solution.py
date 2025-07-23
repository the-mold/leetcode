def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort() # n log n
    n = len(potions)

    res = []
    for spell in spells:
        l, r = 0, n - 1
        
        first_valid_index = n
        while l <= r:
            mid = (l + r) // 2
            product = spell * potions[mid]

            if product >= success:
                first_valid_index = min(mid, first_valid_index)
                r = mid - 1
            else:
                l = mid + 1
        
        res.append(n - first_valid_index)
    
    return res

# T: O(n * log n + m * log n)
# S: O(1)

successfulPairs([5,1,3], [1,2,3,4,5], 7)