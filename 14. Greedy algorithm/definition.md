What is a Greedy Algorithm?
A greedy algorithm is a simple, intuitive approach to problem-solving that makes the locally optimal choice at each stage with the hope of finding a globally optimal solution.

In simpler terms, at every step, the algorithm picks the option that looks best right now, without worrying about the future consequences of that choice. It never reconsiders its past decisions.

A Simple Analogy: Making Change
Imagine you are a cashier and need to give someone 48 cents in change using the fewest possible coins (quarters, dimes, nickels, pennies).

A greedy approach would be:

Step 1: What's the biggest coin I can use? A quarter (25¢). Now I need to give 23¢ more.
Step 2: What's the biggest coin I can use now? A dime (10¢). Now I need 13¢ more.
Step 3: What's the biggest coin now? Another dime (10¢). Now I need 3¢ more.
Step 4: What's the biggest coin? A penny (1¢). Need 2¢.
Step 5: A penny (1¢). Need 1¢.
Step 6: A penny (1¢). Done.
You made the "greedy" choice at each step (the largest coin possible) and ended up with the correct, optimal solution (1 quarter, 2 dimes, 3 pennies).

When Do Greedy Algorithms Work?
Greedy algorithms are fast and simple, but they don't work for every problem. They are only effective for problems that have a special characteristic known as the greedy choice property, which means that a series of locally optimal choices actually does lead to the global optimum.

When they fail: Consider the same change-making problem, but with a strange set of coins: 1¢, 7¢, and 10¢. You need to make 15¢.

Greedy approach: Takes a 10¢ coin. Now needs 5¢. The only option is five 1¢ coins. Total coins: 1 + 5 = 6 coins.
Optimal solution: Takes two 7¢ coins and one 1¢ coin. Total coins: 3 coins.
Here, the greedy choice at the first step (taking the 10¢ coin) prevented the algorithm from finding the true best solution.

How This Applies to the Gas Station Problem
The solution we used for the Gas Station problem is a perfect example of a greedy algorithm.

The Greedy Choice: At each station, we greedily assume that our chosen start_station is the correct one and continue our journey. We add the net gain/loss of gas (gas[i] - cost[i]) to our tank.
The Local Optimum: The "best" choice at each station is to simply keep going, as long as we have enough gas.
The "Forced" Decision: We only change our minds when the situation becomes impossible—that is, when our tank drops below zero. When that happens, we know for a fact that none of the stations we just passed could have been the starting point. So, we make a new greedy choice: we assume the next station (i + 1) is the new best starting point and reset our tank.
Because of the problem's specific nature (if sum(gas) >= sum(cost), a unique solution is guaranteed), this greedy strategy of "keep going until you fail, then start over from the next spot" is guaranteed to find the correct starting station.