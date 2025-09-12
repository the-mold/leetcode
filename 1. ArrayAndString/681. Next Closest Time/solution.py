class Solution(object):
    def nextClosestTime(self, time):
        curr_minutes = 60 * int(time[:2]) + int(time[3:])

        allowed_digits = {x for x in time if x != ":"}
        while True:
            curr_minutes = (curr_minutes + 1) % (24 * 60) # the part with "% (24 * 60)" needed when you go over 23:59. You will be reset back.

            h = curr_minutes // 60
            m = curr_minutes % 60
            candidate_time = f"{h:02d}:{m:02d}"

            candidate_time_no_separator = candidate_time.replace(":", "")
            if all(digit in allowed_digits for digit in candidate_time_no_separator):
                return candidate_time

# T:O(1)
# S:O(1)
