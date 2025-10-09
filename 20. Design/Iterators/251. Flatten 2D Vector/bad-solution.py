# NOTE: it works but it is bad solution.
# One of the main purposes of an Iterator is to minimize the use of auxiliary space. We should try to utilize the existing data structure as much as possible, only adding as much extra space as needed to keep track of the next value. In some situations, the data structure we want to iterate over is too large to even fit in memory anyway (think of file systems).

# In the case of our above implementation, we might as well have just had a single function List<Integer> getFlattenedVector(int[][] v), which would return a List of integers, that could then be iterated over using the List types own standard Iterator.

# As a general rule, you should be very cautious of implementing Iterators with a high time complexity in the constructor, with a very low time complexity in the next() and hasNext() methods. If the code using the Iterator only wanted to access the first couple of elements in the iterated collection, then a lot of time (and probably space) has been wasted!

# As a side note, modifying the input collection in any way is bad design too. Iterators are only allowed to look at, not change, the collection they've been asked to iterate over.


class Vector2D:

    def __init__(self, v: List[List[int]]):
        # We need to iterate over the 2D vector, getting all the integers
        # out of it and putting them into the nums list.
        self.nums = []
        for inner_list in v:
            for num in inner_list:
                self.nums.append(num)
        # We'll keep position 1 behind the next number to return.
        self.position = -1

    def next(self) -> int:
        # Move up to the current element and return it.
        self.position += 1
        return self.nums[self.position]

    def hasNext(self) -> bool:
        # If the next position is a valid index of nums, return True.
        return self.position + 1 < len(self.nums)

# T:O(n) in constructor
# T:O(1) in next and hasNext
# S:O(n)