def canCompleteCircuit(self, gas: list[int], cost: list[int]):
  if sum(gas) < sum(cost):
      return -1

  start_idx = 0
  total_gas = 0
  for i in range(len(gas)):
      total_gas += gas[i] - cost[i]

      if total_gas < 0:
          total_gas = 0
          start_idx = i + 1
  
  return start_idx


#T:O(n)
#S:O(1)


# Intuition
# This problem can be solved in a single pass (O(n) time complexity) using a greedy approach.

# Check for Possibility: A full circuit is only possible if the total amount of gas available is greater than or equal to the total cost of travel. If sum(gas) < sum(cost), it's impossible to complete the journey, so we can immediately return -1.
# Greedy Traversal: We can iterate through the gas stations once, keeping track of the current tank level and a potential starting station.
# We'll maintain a tank variable, which represents the gas we have for the current trip segment.
# We'll also have a start_station index, which we assume is our starting point.
# As we move from one station to the next, we update our tank with the gas[i] - cost[i].
# If at any point our tank drops below zero, it means we cannot reach the next station from our current start_station. Because we've already established that a solution must exist (from step 1), we know that none of the stations we've visited so far in this segment can be the starting station. Therefore, we reset our start_station to the next station (i + 1) and reset our tank to 0, effectively starting a new trip segment.
# Guaranteed Solution: If the loop completes, the start_station we have at the end is the correct one. This is because if a solution exists (and the problem guarantees it is unique if sum(gas) >= sum(cost)), this greedy approach is guaranteed to find it.
