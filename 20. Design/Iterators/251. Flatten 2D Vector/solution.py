class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer_p = 0
        self.inner_p = 0
        
    # If the current outer and inner point to an integer, this method does nothing.
    # Otherwise, inner and outer are advanced until they point to an integer.
    # If there are no more integers, then outer will be equal to vector.length
    # when this method terminates.
    def _advance_to_next(self):
        # While outer is still within the vector, but inner is over the
        # end of the inner list pointed to by outer, we want to move
        # forward to the start of the next inner vector.
        while self.outer_p < len(self.vec) and self.inner_p == len(self.vec[self.outer_p]):
            self.outer_p += 1
            self.inner_p = 0

    def next(self) -> int:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self._advance_to_next()

        # Return current element and move inner so that is after the current
        # element.
        res = self.vec[self.outer_p][self.inner_p]
        self.inner_p += 1
        return res
            

    def hasNext(self) -> bool:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self._advance_to_next()
        
        # If outer = vector.length then there are no integers left, otherwise
        # we've stopped at an integer and so there's an integer left.
        return self.outer_p < len(self.vec)


# T:O(1) constructor,next, hasNext
# T:O(N/V) for _advance_to_next. 
# If the iterator is completely exhausted, then all calls to advanceToNext() will have performed O(N+V) total operations.
# However, because we perform N advanceToNext() operations in order to exhaust the iterator, the amortized cost of this operation is just
# O((N+V/N)) = O(V/N)
