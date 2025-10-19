class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = collections.defaultdict(list)
        in_degrees = [0] * numCourses

        # create adjecency map
        for course, prerequisite in prerequisites:
            adj_map[prerequisite].append(course)
            in_degrees[course] += 1
        
        # add courses to the queue that have no courses that depend on them
        q = collections.deque()
        for idx, course in enumerate(in_degrees):
            if course == 0:
                q.append(idx)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            
            for course_that_depends_on_current_course in adj_map[course]:
                in_degrees[course_that_depends_on_current_course] -= 1
                if in_degrees[course_that_depends_on_current_course] == 0:
                    q.append(course_that_depends_on_current_course)
        
        if len(res) != numCourses:
            return []

        return res


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