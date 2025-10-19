# Definition
Depth first search(DFS) for each node, you take some neighbour and drill down to the end.
Breadth first search(BFS) for each node, you consider all neighbours, then for each neighbor consider all of its neighbours and so one. Usually done with a queue and .popleft()

# Abbreviation
directed acyclic graph (DAG) <- Note: do not check for `seen` in this case.

# Cyclic vs acyclic graph
if a graph has a cycle, it is cyclic otherwise it is acyclic.

# Directed vs undirected graph
Important when building adjecency map: 
if graph is directed then only note start->destination in adjecency map.
If graph is undirected, then ALSO note destination->start in adjecency map.
```
for start, end in graph:
  adjecency_map[start].append(end)
  # only if undirected:
  # adjecency_map[end].append(start)
```

# Representation
Graphs are usually presented as adjecency lists:
{
  <vertice1>: [<vertice2>, <vertice3>]
}
Or less commonly with adjecency matrix, where index is vertice and value of `1` if vertices are connected:
0  1 2 3
1 [0,1,1]
2 [0,0,0]
3 [0,0,0]

# Traversal complexities
Time complexity: O(V + E) , where V is vertices(nodes) and E is edges. Time complexity is sum of all its vertices and its edges. For each vertice you go over all of its vertices and not all graph vertices(which would be O(V*E)).

Space: O(V + E)


Tree is also a graph that is undirected and acyclic(no cycles).


# What is Topological Sort?
Topological sort is a linear ordering of the nodes in a directed graph where for every directed edge from node A to node B, node A comes before node B in the ordering.
So you just list all graph nodes from start to finish.

Why you need it?
1. To Check if a Set of Tasks is Possible (Cycle Detection)
This is exactly the "Course Schedule" problem. The question "Can you finish all courses?" is really asking: "Is there a cycle in the prerequisite graph?"
If a topological sort is possible → No cycle → You can finish the courses.
If a topological sort is impossible → There is a cycle → You cannot finish.
2. To Find a Valid Sequence of Execution
Once you know the tasks are possible, you might need to find an actual order to perform them.
Real-World Applications:
Course Prerequisites: The problem we just solved.
Software Build Systems: A compiler needs to build dependency files (.o) before linking them into the final program (.exe).
Package Management (npm, pip): A package manager must install dependencies before installing the package that needs them.
Project Management: You can't build the walls of a house before laying the foundation.
Spreadsheet Formulas: If cell C1 = A1 + B1, the spreadsheet must calculate A1 and B1 before it can calculate C1. A circular reference (A1=B1, B1=A1) is a cycle, and the spreadsheet will show an error.