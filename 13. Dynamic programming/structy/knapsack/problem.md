Write a function knapsack that takes in a list of item values, a list of item weights, and a weight limit. The i-th item has a value of values[i] and a weight of weights[i]. Your job is to pick items to pack into your knapsack so that its total weight does not exceed the limit and the value of the items is maximized. You may either take an item once or not at all. You cannot take the same item multiple times. Return the maximum total value of items you can pack into the knapsack.

knapsack([5, 4, 9], [6, 1, 15], 20) # -> 13
