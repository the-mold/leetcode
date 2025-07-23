# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        minVersion = float('inf')
        while l <= r:
            mid = (l+r) // 2
            isBad = isBadVersion(mid)
            if isBad:
                minVersion = min(minVersion, mid)
                r = mid - 1
            else:
                l = mid + 1

        return minVersion
    
#T:O(log n)
#S:O(1)
