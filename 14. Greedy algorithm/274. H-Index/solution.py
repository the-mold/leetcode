class Solution:
  def hIndex(self, citations: List[int]) -> int:
    citations.sort(reverse=True)

    res = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res = max(res, i + 1)
    
    return res

# T:O(n log n)
# S:O(1)

# Intuition
# Yes, the solution you've provided for the H-Index problem is a classic example of a greedy algorithm.

# Let's break down why:

# The Greedy Choice: The core idea is to sort the citations in descending order. This is the "greedy" first step: you are arranging the problem in a way that lets you make simple, sequential decisions. By sorting, you decide to process the most-cited papers first.
# Local Optimality: The algorithm then iterates through this sorted list. At each step i, it makes a simple, locally optimal check: "Do I have at least i + 1 papers that are each cited at least i + 1 times?"
# The condition citations[i] >= i + 1 perfectly captures this.
# Because the list is sorted, if the (i+1)-th paper (citations[i]) meets this bar, you automatically know the i papers before it also do.
# You are greedily trying to increase your candidate for the h-index (i + 1) as long as the condition holds.
# Achieving Global Optimum: The moment the condition citations[i] >= i + 1 fails, the loop can stop (or in this case, continue without updating the result). You know that no larger h-index is possible, because for any subsequent paper, the number of citations will be even lower and the required number of papers will be higher. The series of locally optimal choices (incrementing the potential h-index) leads directly to the globally optimal solution.
