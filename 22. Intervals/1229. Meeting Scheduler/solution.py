class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        p1 = 0
        p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            left_intersect = max(slots1[p1][0], slots2[p2][0])
            right_intersect = min(slots1[p1][1], slots2[p2][1])

            if right_intersect - left_intersect >= duration:
                return [left_intersect, left_intersect + duration]

            # move pointer that ends earlier
            if slots1[p1][1] > slots2[p2][1]:
                p2 +=1
            else:
                p1 += 1
        
        return []
                
# slots1 = [[10,50],[60,120],[140,210]]
#                      p1
# slots2 = [[0,15],[60,70]]
#                      p2

# T:O(nlogn + mlogm + n + m)
# S:(n+m) for sorting
