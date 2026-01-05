province sizes
Write a function, provinceSizes, that takes in a number of cities n and a list of roads which connect cities. Roads can be traveled in both directions. Cities are named from 0 to n.

A "province" is a group of 1 or more cities that are connected by roads. The "size" of a province is the number of cities that make up that province.

Your function should return a list containing the sizes of the provinces. You may return the result in any order.

Solve this using Union-Find.

province_sizes(6, [
  (4, 5),
  (1, 0),
  (2, 3),
  (0, 5),
  (5, 1),
  (4, 0)
]) # -> [4, 2]
