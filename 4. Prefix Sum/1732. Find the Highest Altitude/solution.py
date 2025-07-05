def largestAltitude(gain: List[int]) -> int:
    max_altitude = 0
    current_sum = 0
    for i in range(len(gain)):
        current_sum += gain[i]
        max_altitude = max(max_altitude, current_sum)

    return max_altitude

#T:O(n)
#S:O(1)