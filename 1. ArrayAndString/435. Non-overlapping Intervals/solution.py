class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0
        l = 1
        prev_end = intervals[0][1]
        while l < len(intervals):
            if prev_end > intervals[l][0]:
                count += 1
            else:
                prev_end = intervals[l][1]
            
            l += 1

        return count

# T:O(n)
# S:O(1)

# Trick: sort items by end and not start how it is done usually with intervals. You want to prioritise smaller end value because it will preserve more elemnts 
# of array, hence you need to delete less elements.
