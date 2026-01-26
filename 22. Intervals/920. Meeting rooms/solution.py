class Solution:
  def solve(self, meetings):
    if len(meetings) <= 1:
      return True
    
    meetings.sort(key=lambda x: x.start)
    
    prev_end = meetings[0].end
    for m in meetings[1:]:
      if prev_end > m.start:
        return False
      prev_end = m.end
    
    return True
  