class Solution:
  def solve(self, input):
    if not input:
      return 0
    
    max_rooms = 0
    for i in range(len(input)):
      curr_rooms = 1
      for j in range(len(input)):
        if i == j:
          continue
        # unordered intervals [a,b] [c,d] intercept if b > c and a < d
        # Note: a < d is needed when interval2 is entirely before the interval 1.
        if input[i][1] > input[j][0] and input[j][1] > input[i][0]:
          curr_rooms += 1
      
      max_rooms = max(max_rooms, curr_rooms)
    
    return max_rooms
  
Solution().solve([[0,30],[5,10],[15,20]])

#0---------------------30
#   5---10
#            15---20


# Example why a < d is needed:
# [a,b] [c,d] --- b > c and d > a

# 1: [5,10]
# 2: [1, 4]
# 1-4
#     5--10  # not overlap!
