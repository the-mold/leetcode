class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)

        max_seq = 0
        for num in snums:
            # check if the num is the start of the sequence
            if num - 1 in snums:
                continue

            seq = num
            curr_arr = 0
            while seq in snums:
                curr_arr += 1
                seq += 1

            max_seq = max(max_seq, curr_arr)
        
        return max_seq

#T:O(n)
#S:O(n)

#================================
#Explanation why it is T:O(n) even though there is a nested while loop:
# For loop skips all numbers that are not start of a sequence by checking if n -1 in set.


#More details:
#At first glance, the nested while loop in this solution does look like it could be more than O(n). But let's walk through exactly why this algorithm is still O(n) overall, even with the while loop.

# 🧠 Key Concept: Each number is visited at most once in the inner loop
# Here’s the relevant part of the code again:

# python
# Kopieren
# Bearbeiten
# for num in num_set:
#     if num - 1 not in num_set:  # only start new sequence if num is the beginning
#         current = num
#         streak = 1

#         while current + 1 in num_set:
#             current += 1
#             streak += 1
# 🔍 Why It’s O(n)
# The outer for loop runs once per unique number: O(n).

# The while current + 1 in num_set only runs when num is the start of a sequence.

# Inside that loop, current increases only by 1, and we never revisit the same number again as part of any other sequence.

# Example:
# For input:
# nums = [100, 4, 200, 1, 3, 2]
# The set is: {1, 2, 3, 4, 100, 200}

# Only 1, 100, and 200 are starts of sequences:

# For 1: the while loop runs 3 times (to count 2, 3, 4)

# For 100: runs 0 times

# For 200: runs 0 times

# All other numbers (2, 3, 4) are not starts of a sequence, so they're skipped by the if num - 1 not in num_set check.

# Thus, each number is checked at most twice:

# Once in the for loop

# Once in the while loop (as part of a sequence)

# Even though there's a while inside a for, the total number of times the inner loop runs across all iterations is at most n, where n is the number of unique elements.
