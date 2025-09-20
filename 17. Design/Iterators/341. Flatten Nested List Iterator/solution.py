# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self.list.append(nested_integer.getInteger())
                else:
                    flatten(nested_integer.getList())

        self.list = []
        self.pointer = -1
        # populate the list
        flatten(nestedList)
    
    def next(self) -> int:
        self.pointer += 1
        return self.list[self.pointer]
            
    def hasNext(self) -> bool:
         return self.pointer + 1 < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# Time complexiy
# Constructor: O(N+L).

# The constructor is where all the time-consuming work is done.

# For each list within the nested list, there will be one call to flattenList(...). The loop within flattenList(...) will then iterate n times, where n is the number of integers within that list. Across all calls to flattenList(...), there will be a total of N loop iterations. Therefore, the time complexity is the number of lists plus the number of integers, giving us O(N+L).
# Notice that the maximum depth of the nesting does not impact the time complexity.

# next(): O(1).
# Getting the next element requires incrementing position by 1 and accessing an element at a particular index of the integers list. Both of these are O(1) operations.

# hasNext(): O(1).
# Checking whether or not there is a next element requires comparing the length of the integers list to the position variable. This is an O(1) operation.
# Space complexity : O(N+D).
# The most obvious auxiliary space is the integers list. The length of this is O(N).
# The less obvious auxiliary space is the space used by the flattenList(...) function. Recall that recursive functions need to keep track of where they're up to by putting stack frames on the runtime stack. Therefore, we need to determine what the maximum number of stack frames there could be at a time is. Each time we encounter a nested list, we call flattenList(...) and a stack frame is added. Each time we finish processing a nested list, flattenList(...) returns and a stack frame is removed. Therefore, the maximum number of stack frames on the runtime stack is the maximum nesting depth, D.
