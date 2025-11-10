class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            count += 1
            r -= 1
        
        return count

#T:O(n logn)
#S:O(1)
