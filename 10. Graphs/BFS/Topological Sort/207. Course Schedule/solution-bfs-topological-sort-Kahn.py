# Kahn's Algorithm:

# Start with nodes having no incoming edges (no prerequisites)
# Remove nodes with no prerequisites from the queue. Update in-degrees if you complete the course.
# If we can't remove all nodes, there's a cycle
# Time: O(V + E), Space: O(V + E)

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # --- Step 1: Build the Graph and In-Degree Array ---
        
        # 'graph' will store: {prereq: [courses that depend on it]}
        # e.g., {0: [1, 2]} means finishing 0 unlocks 1 and 2.
        graph = defaultdict(list)
        
        # 'in_degree' will store the number of prerequisites for each course.
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            # Add an edge from the prerequisite to the course.
            graph[prereq].append(course)
            # Increment the prerequisite count for the course.
            in_degree[course] += 1
            
        # --- Step 2: Find the Starting Points ---
        
        # Create a queue and add all courses that have no prerequisites (in-degree of 0).
        # These are the courses we can take right away.
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # --- Step 3: Process Courses and Reduce In-Degrees ---
        
        # 'completed_courses' will count how many courses we can successfully finish.
        completed_courses = 0
        
        # This is the main BFS loop.
        while queue:
            # Take a course from the queue that we are now able to complete.
            course = queue.popleft()
            completed_courses += 1
            
            # Now that we've "completed" this course, it's no longer a prerequisite
            # for other courses. So, we find all courses that depended on it...
            for dependent_course in graph[course]:
                # ...and decrease their prerequisite count (in-degree).
                in_degree[dependent_course] -= 1
                
                # If a dependent course now has 0 prerequisites, it means we can
                # take it. Add it to the queue to be processed.
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
                    
        # --- Step 4: Check if All Courses Were Completed ---
        
        # If the number of courses we were able to complete equals the total number
        # of courses, it means there was no cycle and we can finish everything.
        # If not, there must have been a cycle that left some courses with an
        # in-degree > 0, so they never got added to the queue.
        return completed_courses == numCourses


# Time Complexity: O(V + E)
# This is because every node (vertex) and every edge is processed a constant number of times.

# Graph and In-Degree Construction (O(V + E)):
# Initializing in_degree takes O(V) time.
# The loop to build the graph and in_degree array runs E times (once for each prerequisite). This part is O(E).
# Total for this step: O(V) + O(E) = O(V + E).
# Initializing the Queue (O(V)):
# The loop to find the initial courses with an in-degree of 0 runs V times.
# Main BFS Loop (O(V + E)):
# The while queue: loop will execute exactly V times in a graph without cycles, as each course is enqueued and dequeued exactly once.
# The inner for dependent_course in graph[course]: loop will, over the entire execution of the algorithm, iterate through each edge exactly once. The total number of these iterations across all nodes is E.
# Therefore, the combined work of the while and for loops is O(V + E).
# Combining these steps, the total time complexity is O(V + E) + O(V) + O(V + E), which simplifies to O(V + E).

# Space Complexity: O(V + E)
# This is determined by the storage required for the graph and auxiliary data structures.

# Graph (graph) (O(V + E)):
# The adjacency list stores every edge (E) in the graph. It also requires space for every vertex that has an outgoing edge (up to V). The total space is O(V + E).
# In-Degree Array (in_degree) (O(V)):
# This is an array of size V to store the in-degree for each course.
# Queue (queue) (O(V)):
# In the worst-case scenario (e.g., a graph with one node connected to all others), the queue could hold up to V-1 nodes at one time. The space is O(V).
# The dominant factor is the adjacency list, so the total space complexity is O(V + E).