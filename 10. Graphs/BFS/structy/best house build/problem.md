You are building a new house in the neighborhood and want to choose a location so that the house is as close as possible to all other houses.

Write a function, best_house_build, that takes in a grid. In the grid, 0's are empty spaces, 1's are houses, and 2's are trees. Your job is to find an empty space on the grid that has the shortest total travel distance to all houses. Your function should return a number that corresponds to this shortest total travel distance. If it is not possible to choose a location that is that is reachable by all houses, then return -1.

When calculating the distance, you can only move up, down, left, or right. You may not pass through houses or trees.