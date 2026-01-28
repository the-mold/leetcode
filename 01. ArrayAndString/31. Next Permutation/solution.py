# Intuition: remember that you are looking for the next SORTED permutation.
# To find next sorted permutation:
#1. Find the pivot element. This is the element that we could exchange by some other element on the right.
# Formula to find pivot: got from right to start. Find the element where nums[i] < nums[i+1]. It means that we could change the element by at least i+1.
# Example 1:
# [1,2,3]
#    P
# To get next sorted permutation, we can change 2 by 3 because lexilogically [1,3,2] comes after [1,2,3].

# Example 2:
# [2,1,5,4,3,0]
#    P 

# 2. Find the smallest element from the right that is greater than nums[pivot_idx] and exchange it.

# 3. Sort all numbers from the right of the pivot element. Because the right side is sort of sorted already in descending order,
# you can achieve sorting in asc order by reversing the right side.

# Example walkthrough:
#Step 1:
# [2,1,5,4,3,0]
#    P 
#Step 2:
# [2,3,5,4,1,0]
#    P 
#Step 3:
#Reverse the right side [5,4,1,0] which results in:
# [2,3,0,1,4,5]
#    P 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. Find pivot: first i from the right with nums[i-1] < nums[i]
        pivot = float("inf")
        for i in range(n -1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i-1
                break

        # edge case
        if pivot == float("inf"):
            # our input array was already ordered in decreasing order. Just return the reverse of the input array
            self.reverse(nums, 0)
            return

        # 2. Find rightmost element greater than nums[pivot] and swap
        for i in range(n-1, pivot, -1):
            if nums[pivot] < nums[i]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break

        # 3. reverse the rest of subarray on the right of pivor
        self.reverse(nums, pivot+1)

    def reverse(self, nums, start):
        l, r = start, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# T:O(n)
# S:O(1)




# Algorithm

# First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
# For example, no next permutation is possible for the following array:

# [9, 5, 4, 3, 1]
# We need to find the first pair of two successive numbers a[i] and a[i−1], from the right, which satisfy
# a[i]>a[i−1]. Now, no rearrangements to the right of a[i−1] can create a larger permutation since that subarray consists of numbers in descending order.
# Thus, we need to rearrange the numbers to the right of a[i−1] including itself.

# Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number a[i−1] with the number which is just larger than itself among the numbers lying to its right section, say a[j].

#  Next Permutation 

# We swap the numbers a[i−1] and a[j]. We now have the correct number at index i−1. But still the current permutation isn't the permutation
# that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of a[i−1]. Therefore, we need to place those
# numbers in ascending order to get their smallest permutation.

# But, recall that while scanning the numbers from the right, we simply kept decrementing the index
# until we found the pair a[i] and a[i−1] where, a[i]>a[i−1]. Thus, all numbers to the right of a[i−1] were already sorted in descending order.
# Furthermore, swapping a[i−1] and a[j] didn't change that order.
# Therefore, we simply need to reverse the numbers following a[i−1] to get the next smallest lexicographic permutation.