You are given the tolls for different highways. Each highway connects a pair of cities and has a particular cost that must be paid to use it.

Each highway toll is a triplet (cityA, cityB, cost). Every highway can be traveled in either direction.

Write a function that takes in highway tolls and two cities. The function should return the lowest cost required to travel between the two cities. You can assume that there exists at least one way to travel between the two cities.

highway_tolls = [
  ("Hampton", "Fairfax", 7.50),
  ("Roanoake", "Alexandria", 4.20),
  ("Alexandria", "Hampton", 14.50),
  ("Hampton", "Roanoake", 8.90),
  ("Alexandria", "Fairfax", 5.90),
  ("Hampton", "Manassas", 3.50),
  ("Fairfax", "Manassas", 2.20),
]
lowest_toll(highway_tolls, "Alexandria", "Hampton") # -> 11.60
