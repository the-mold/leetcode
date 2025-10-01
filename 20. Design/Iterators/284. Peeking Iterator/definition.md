Overview - What is an Iterator?
Feel free to skip this section if you're already familiar with this material. We have included it, as this is a beginners question on iterators.

If you've heard of Iterators, you might assume they're simply a way of iterating over indexed or finite data structures. You've probably used them in loops, e.g. for item in items: in Python or for (int num : nums) in Java.

This may make it seem strange that we would need a .peek() on an Iterator. After all, couldn't we just convert our data structure into an array and use indexing to peek?

But actually Iterators have some interesting properties that make them widely useful for not only indexed collections (e.g. Array) and other finite data structures (e.g. LinkedList or HashMap keys), but also for (possibly-infinite) generated data. We'll look at an example of that soon.

The first property of an Iterator that we'll looked at is that it only needs to know how to get the next item. It doesn't need to store the entire data in memory if we don't need the entire data structure. For massive data structures, this is invaluable!

For example consider a linked list Iterator. We'll use Python as it's nice and compact. The same ideas apply to Java and C++:

class LinkedListIterator:
    def __init__(self, head):
        self._node = head

    def hasNext(self):
        return self._node is not None

    def next(self):
        result = self._node.value
        self._node = self._node.next
        return result
Notice how we store the head at the start, but as items are consumed, we discard the current one and replace it with the item in the node after?

This means that if we're simply iterating a Linked List, and don't ever need to go back to the head, then we only need to keep one value around at a time.

Another really interesting property of Iterators is that they can represent sequences without even using a data structure!

For example consider a range Iterator:

class RangeIterator:
    def __init__(self, min, max):
        self._max = max
        self._current = min

    def hasNext(self):
        return self._current < self._max

    def next(self):
        self._current += 1
        return self._current - 1
If we simply converted this to an Array, we'd need to allocate a large chunk of memory if min and max are far apart. For the most part, this would probably be wasted space.

However, by using an Iterator, we can use features like for i in range(40, 20000000) while still retaining the O(1) space of classic for (int i = min; i < max; i++) style loops seen in other languages.

Our final property is one that we couldn't even do by copying values into an Array—handling an infinite sequence. For example consider an Iterator of squares:

class SquaresIterator:
    def __init__(self):
        self._n = 0

    def hasNext(self):
        # It continues forever,
        # so definitely has a next!
        return True

    def next(self):
        result = self._n
        self._current += 1
        return result ** 2
Notice that because .hasNext() always returns True, this Iterator will never run out of items. And this is to be expected, there's always another square after the previous, so our Iterator can give as many as we ask from it.

Now that we've looked at why Iterators are awesome, let's consider what they are at a base level.

An Iterator only provides two methods:

.next()
This returns the next item in the sequence. You can't assume that this item actually "exists" yet, it might be created when you call .next(), or it might already exist in a data structure that you have an Iterator over.

Once .next() is called, it will update the state of the Iterator. This means once you've got a value from .next() you won't be able to get the same value again. Therefore, if you don't store or process the value you got from the Iterator then it's possibly gone forever!

.hasNext()
This returns whether or not another item is available. For example, an array Iterator should return False if we're at the end of the array. But for an Iterator that can produce items indefinitely, such as our square generator above, it might never return False.

A further property of Iterators is that they provide a clean interface for the code using them. Without Iterators, Linked List's, for example, tend to be particularly messy, as the code for traversing them gets muddled within the application code. With an Iterator, the external code doesn't even know how the underlying data structure works. For all it knows, the data could be coming from a Linked List, an Array, a Tree, a State Machine, a clever number generator, a file reader, a robot sensor, etc.

Not having to deal with nodes, state, indexes, etc leads to clean code. We call this the Iterator Pattern, and it is one of the most important design patterns for a software engineer to know.

As shown above, with only two methods, we get a lot of benefit (e.g. infinite sequences) and increased performance (e.g. not expanding sequences like range into arrays). We also get a nice way of separating the underlying data structure from the code that uses it.