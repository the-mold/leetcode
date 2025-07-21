class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        q = [0]

        #At the beginning, we have a todo list "q" of keys to use.
        #'visited' represents at some point we have entered this room.
        while q:    #While we have keys...
            node = q.pop(0)        # get the next key 'node'

            for key in rooms[node]:     # For every key in room # 'node'...
                if not visited[key]:    # ... that hasn't been used yet
                    visited[key] = True # mark that we've entered the room
                    q.append(key)       # add the key to the todo list
        
        return all(visited) # Return true if we've visited every room
    
  
# Time Complexity: O(N²)
# The main reason for this complexity is the line node = q.pop(0).

# Queue Implementation: The code uses a standard Python list as a queue. While append (adding to the end) is fast (amortized O(1)), pop(0) (removing from the beginning) is very slow.
# Why pop(0) is slow: To remove the first element from a list, Python must shift all subsequent elements one position to the left. If the list has k elements, pop(0) takes O(k) time.
# Overall Impact: In the worst case, the queue q can grow to hold nearly N rooms. Popping from a large queue repeatedly leads to a quadratic time complexity. The total work done by all pop(0) operations approaches O(N²). The work for iterating through all keys is still O(E), but this is overshadowed by the queue operations.
# Therefore, the total time complexity is O(N² + E), which simplifies to O(N²) because in a dense graph, E could be on the order of N². This is less efficient than the O(N + E) solution that uses collections.deque.

# Space Complexity: O(N)
# The space complexity is the same as my solution.

# visited list: This list stores N boolean values, so it requires O(N) space.
# q list (queue): In the worst case, the queue can hold up to N rooms. This also requires O(N) space.