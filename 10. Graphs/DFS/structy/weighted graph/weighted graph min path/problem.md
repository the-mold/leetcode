Write a function that takes in the adjacency list for a weighted graph and two nodes, src and dst. The function should return the minimum cost path that travels from src to dst.

The cost of a path is the sum of the weights of edges traveled.

You can assume that the weights are non-negative numbers and there is at least one path between src and dst.

graph = {
  "a": { "b": 2, "d": 9, "c": 5 },
  "b": { "a": 2, "d": 4, "e": 6 },
  "c": { "a": 5, "e": 4 },
  "d": { "a": 9, "b": 4, "e": 1 },
  "e": { "b": 6, "c": 4, "d": 1 },   
}
weighted_graph_min_path(graph, "a", "e") # -> 7
