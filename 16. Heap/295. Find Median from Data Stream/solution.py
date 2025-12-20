import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []    # max heap (use negative values)
        self.hi = []    # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)                    # Add to max heap
        
        heapq.heappush(self.hi, -heapq.heappop(self.lo))  # balancing step
        
        if len(self.lo) < len(self.hi):                  # maintain size property
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) > len(self.hi) else (-self.lo[0] + self.hi[0]) * 0.5

# Time complexity: O(5⋅logn)+O(1)≈O(logn).

# At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about O(logn) time.
# Finding the median takes constant O(1) time since the tops of heaps are directly accessible.
# Space complexity: O(n) linear space to hold input in containers.


# Intuition

# The above two approaches gave us some valuable insights on how to tackle this problem. Concretely, one can infer two things:

# If we could maintain direct access to median elements at all times, then finding the median would take a constant amount of time.
# If we could find a reasonably fast way of adding numbers to our containers, additional penalties incurred could be lessened.
# But perhaps the most important insight, which is not readily observable, is the fact that we only need a consistent way to access the median elements. Keeping the entire input sorted is not a requirement.

# Well, if only there were a data structure which could handle our needs.

# As it turns out there are two data structures for the job:

# Heaps (or Priority Queues 1)
# Self-balancing Binary Search Trees (we'll talk more about them in Approach 4)
# Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic order of time. They also give direct access to the maximal/minimal elements in a group.

# If we could maintain two heaps in the following way:

# A max-heap to store the smaller half of the input numbers
# A min-heap to store the larger half of the input numbers
# This gives access to median values in the input: they comprise the top of the heaps!

# Wait, what? How?

# If the following conditions are met:

# Both the heaps are balanced (or nearly balanced)
# The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers
# then we can say that:

# All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it x)
# All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it y)
# Then x and/or y are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.

# This leads us to a huge point of pain in this approach: balancing the two heaps!

# Algorithm

# Two priority queues:

# A max-heap lo to store the smaller half of the numbers
# A min-heap hi to store the larger half of the numbers
# The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed k elements:

# If k=2∗n+1(∀n∈Z), then lo is allowed to hold n+1 elements, while hi can hold n elements.
# If k=2∗n(∀n∈Z), then both heaps are balanced and hold n elements each.
# This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.

# Adding a number num:

# Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. So remove the largest element from lo and offer it to hi.
# The min-heap hi might end holding more elements than the max-heap lo, after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.
# The above step ensures that we do not disturb the nice little size property we just mentioned.

# A little example will clear this up! Say we take input from the stream [41, 35, 62, 5, 97, 108]. The run-though of the algorithm looks like this:

# Adding number 41
# MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
# MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
# Median is 41
# =======================
# Adding number 35
# MaxHeap lo: [35]
# MinHeap hi: [41]
# Median is 38
# =======================
# Adding number 62
# MaxHeap lo: [41, 35]
# MinHeap hi: [62]
# Median is 41
# =======================
# Adding number 4
# MaxHeap lo: [35, 4]
# MinHeap hi: [41, 62]
# Median is 38
# =======================
# Adding number 97
# MaxHeap lo: [41, 35, 4]
# MinHeap hi: [62, 97]
# Median is 41
# =======================
# Adding number 108
# MaxHeap lo: [41, 35, 4]
# MinHeap hi: [62, 97, 108]
# Median is 51.5
