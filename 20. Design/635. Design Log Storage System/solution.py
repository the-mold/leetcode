# Intuition: convert timestamp into seconds and filter by it.

class LogSystem:

    def __init__(self):
        self.logs = []
        self.start_epoche = 1999
        self.granularity_idx = {
            "Year": 0, 
            "Month": 1, 
            "Day": 2, 
            "Hour":3, 
            "Minute":4, 
            "Second":5 
        }

    def _convert(self, segments):
        # convert each segment to milliseconds

        year_sec = (int(segments[0]) - self.start_epoche) * 12 * 31 * 24 * 60 * 60
        month_sec = int(segments[1]) * 31 * 24 * 60 * 60
        day_sec = int(segments[2]) * 24 * 60 * 60
        hour_sec = int(segments[3]) * 60 * 60
        minute_sec = int(segments[4]) * 60
        seconds = int(segments[5])

        return year_sec + month_sec + day_sec + hour_sec + minute_sec + seconds


    def put(self, id: int, timestamp: str) -> None:
        segments = timestamp.split(":")
        timestamp_int = self._convert(segments)
        self.logs.append((timestamp_int, id))

    def _convert_with_granularity(self, ts, granularity, is_end):
        gran_idx = self.granularity_idx[granularity]
        ts = ts.split(":")

        res = [self.start_epoche, 1, 1, 0, 0, 0]

        for i in range(gran_idx+1):
            res[i] = int(ts[i])
        
        # If calculating the end of the range, increment the relevant part
        # to create an exclusive upper bound.
        if is_end:
            res[gran_idx] += 1

        return self._convert(res)


    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start = self._convert_with_granularity(start, granularity, False)
        end = self._convert_with_granularity(end, granularity, True)

        res = []
        for ts, id in self.logs:
            if start <= ts < end:
                res.append(id)
        
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)