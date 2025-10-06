class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        for idx, value in enumerate(self.prefix_sums):
            if target < value:
                return idx
        


# Let N be the length of the input list.

# Time Complexity

# For the constructor function, the time complexity would be O(N), which is due to the 
# construction of the prefix sums.


# For the pickIndex() function, its time complexity would be O(N) as well, since we did a 
# linear search on the prefix sums.


# Space Complexity

# For the constructor function, the space complexity would be O(N), which is again due to the 
# construction of the prefix sums.


# For the pickIndex() function, its space complexity would be O(1), since it uses constant memory. 
# Note, here we consider the prefix sums that it operates on, as the input of the function.