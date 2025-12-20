class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_largest():
            idx_to_pop = stones.index(max(stones))
            return stones.pop(idx_to_pop)

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 > stone_2:
                stones.append(stone_1 - stone_2)
        
        return stones[0] if len(stones) > 0 else 0

# Let N be the length of stones. Here on LeetCode, we're only testing your code with cases where N≤30. In an interview though, be very careful about such assumptions. It is very likely your interviewer expects you to come up with the best possible algorithm you could (thus handling the highest possible value of N you can).

# Time complexity : O(N ** 2).

# The only non-O(1) method of StoneArray is findAndRemoveMax(). This method does a single pass over the array, to find the index of the maximum value. This pass has a cost of O(N). Once we find the maximum value, we delete it, although this only has a cost of O(1) because instead of shuffling along, we're simply swapping with the end.

# Each time around the main loop, there is a net loss of either 1 or 2 stones. Starting with N stones and needing to get to 1 stone, this is up to N−1 iterations. On each of these iterations, it finds the maximum twice. In total, we get O(N**2).

# Note that even if we'd shuffled instead of swapped with the end, the findAndRemoveMax() method still would have been O(N), as the pass and then deletion are done one-after-the-other. However, it's often best to avoid needlessly large constants.

# Space complexity : O(N) or O(1).

# For the Python: We are not allocating any new space for data structures, and instead are modifying the input list. Note that this modifies the input. This has its pros and cons; it saves space, but it means that other functions can't use the same array.

# For the Java: We need to convert the input to an ArrayList, and therefore the ints to Integers. It is possible to write a O(1) space solution for Java, however it is long-winded and a lot of work for what is a poor overall approach anyway.