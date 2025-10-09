class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0

# Let N be the length of stones.

# Time complexity : O(NlogN).

# Converting an array into a Heap takes O(N) time (it isn't actually sorting; it's putting them into an order that allows us to get the maximums, each in O(logN) time).

# Like before, the main loop iterates up to N−1 times. This time however, it's doing up to three O(logN) operations each time; two removes, and an optional add. Like always, the three is an ignored constant. This means that we're doing N⋅O(logN)=O(NlogN) operations.

# Space complexity : O(N) or O(logN).

# In Python, heapq.heapify() is an in-place operation, so it uses O(1) auxiliary space. However, the heap still stores n elements within the input list, which contributes O(n) to total space complexity. So, the total space complexity is O(n).

# In Java though, it's O(N) to create the PriorityQueue.

# We could reduce the space complexity to O(1) by implementing our own iterative heapfiy, if needed.

