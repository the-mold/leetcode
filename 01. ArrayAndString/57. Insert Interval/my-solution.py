class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # not need to sort here but as reminder how to do it
        # intervals.sort(key=lambda x: x[0])
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]

        # 1. the new element where needed
        is_inserted = False
        for idx, value in enumerate(intervals):
            start, end = value
            if start > newInterval[0]:
                if idx == 0:
                    intervals.insert(0, newInterval)
                else:
                    intervals.insert(idx, newInterval)

                is_inserted = True
                break

        if not is_inserted:
            intervals.append(newInterval)


        # 2. merge all overlapping elements
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if start > prev_end:
                res.append([start, end])
            else:
                res[-1][1] = max(end, prev_end)

        return res
