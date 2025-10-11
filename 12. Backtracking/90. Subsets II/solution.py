# Warning! You must sor the inlut array

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = []
        currentSubset = []
        self.subsetsWithDupHelper(subsets, currentSubset, nums, 0)
        return subsets

    def subsetsWithDupHelper(self, subsets, currentSubset, nums, index):
        # Add the subset formed so far to the subsets list.
        subsets.append(list(currentSubset))
        for i in range(index, len(nums)):
            # Skip duplicates: if current element is same as previous
            # and we're not at the start position, skip it
            if i != index and nums[i] == nums[i - 1]:
                continue
            currentSubset.append(nums[i])
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i + 1)
            currentSubset.pop()
    
# Complexity Analysis

# Here n is the number of elements present in the given array.

# Time complexity: O(n⋅2**n)

# As we can see in the diagram above, this approach does not generate any duplicate subsets. Thus, in the worst case (array consists of n distinct elements), the total number of recursive function calls will be 2**n. 
# Also, at each function call, a deep copy of the subset currentSubset generated so far is created and added to the subsets list. This will incur an additional O(n) time (as the maximum number of elements in the currentSubset will be n). So overall, the time complexity of this approach will be O(n⋅2(**n).

# Space complexity: O(n)

# The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, the Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is O(logn). In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort and Insertion Sort with the worst case space complexity of O(logn). Thus the use of inbuilt sort() function adds O(logn) to space complexity.

# The recursion call stack occupies at most O(n) space. The output list of subsets is not considered while analyzing space complexity. So, the space complexity of this approach is O(n).
