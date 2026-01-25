class Solution:
    def is_intersect(self, s1, s2):
        # [a,b] [c,d]: a < d and b > c
        return s1[0] < s2[1] and s1[1] > s2[0]

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        for i in range(len(slots1)):
            for j in range(len(slots2)):
                s1 = slots1[i]
                s2 = slots2[j]
                if self.is_intersect(s1, s2):
                    common_avail = [max(s1[0], s2[0]), min(s1[1],s2[1])]
                    d = common_avail[1] - common_avail[0]
                    if d >= duration:
                        return [common_avail[0], common_avail[0] + duration]
        return []

# T:O(nm)
# S:(n + m) from sorting


# s1: [[10,50],[60,120],[140,210]]
# s2: [[0,15],[60,70]]
# D:8

#    10----------50    60----------120.    140----------210
#0-------15            60-----70


# [a,b] [c, d] -> a < d and b > c
# [10,50].  a(10) < d(15)
# [0,15].   b(50) > c(0)

# intersect match - [max(s1, s2), min(e1, e2)].  -> [10, 15] -> duration < d -> move on
#                                                            -> duration >= d -> return [start, start+d]

        #slots1.sort(key=lambda x: x[0])
        #slots2.sort(key=lambda x: x[0])
