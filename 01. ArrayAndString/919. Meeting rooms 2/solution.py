class Solution:
  def solve(self, meetings):
    if len(meetings) == 0:
      return 0
    
    # Create events: (time, type) where type=1 for start, type=-1 for end
    events = []
    for start, end in meetings:
      events.append((start, 1))
      events.append((end, -1))
      
    # Sort events by time (if same time, process ends before starts. First rooms is emptied -1 and then filled again)
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_rooms = 0
    curr_rooms = 0
    
    for _, event_type in events:
      curr_rooms += event_type
      max_rooms = max(max_rooms, curr_rooms)
    
    return max_rooms

Solution().solve([[0,30],[5,10],[15,20]])
