class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = collections.defaultdict(list)
        for course, prereq in prerequisites:
            # Why use prereq as key in adj_map?
            # We need to check: "If I finish this prerequisite, what courses become available?"
                # My Mapping: prereq → [courses that depend on it]
                # python
                # # prerequisites = [[1,0], [2,0], [3,1]]
                # # Meaning: course 1 needs 0, course 2 needs 0, course 3 needs 1

                # graph = {
                #     0: [1, 2],  # After finishing course 0, you can take courses 1 and 2
                #     1: [3]      # After finishing course 1, you can take course 3
                # }
            adj_map[prereq].append(course) 

        # here i track if i there is a cycle
        state = [0] * numCourses

        def has_cycle(course_idx):
            # cycle detected
            if state[course_idx] == 1:
                return True
            # course was checked already, there is not cycle
            if state[course_idx] == 2:
                return False

            # mark in state that you are checking course now
            state[course_idx] = 1

            dependents = adj_map[course_idx]
            for dep in dependents:
                if has_cycle(dep):
                    return True
            
            # mark course as checked and with no cycles
            state[course_idx] = 2

            return False

        for i in range(numCourses):
            # test only courses you did not check yet
            if state[i] == 0:
                if has_cycle(i):
                    return False
        
        return True


# Time	O(V + E)	Each node/edge visited once
# Space	O(V + E)	Adjacency list + state array + recursion stack