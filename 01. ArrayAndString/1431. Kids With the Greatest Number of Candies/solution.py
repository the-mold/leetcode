def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    current_max = max(candies)    #O(n)
    res = []
    for can in candies:    #O(n)
        if can + extraCandies >= current_max:
            res.append(True)
        else:
            res.append(False)

    return res    

#T:O(n)
#S:O(1)