class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort(key=lambda x: x[0])

        merged = [meetings[0]]
        for start, end in meetings[1:]:
            prev_start = merged[-1][0]
            prev_end = merged[-1][1]

            if prev_end < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        count = 0
        # before
        if merged[0][0] > 0:
            count += merged[0][0] - 1

        # middle
        prev_end = merged[0][1]
        for start, end in merged[1:]:
            if (prev_end + 1) < start:
                count += start - prev_end - 1
            prev_end = end
        
        # end
        count += days - merged[-1][1]

        return count
        
# T: O(n logn)
# S: O(n)
