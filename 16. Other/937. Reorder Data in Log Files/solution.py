class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_sort_key(log):
            identifier, content = log.split(" ", maxsplit=1)

            if content[0].isalpha():
                # If it's a letter-log (i.e., content starts with an alphabetic character),
                # we want it sorted by (0, content, identifier) to ensure that it appears
                # before any digit-logs and that letter-logs are sorted firstly by content
                # and secondly by identifier if there's a tie in content.
                return (0, content, identifier)
            else:
                # If it's a digit-log (i.e., content starts with a digit),
                # we use (1,) so that it appears after all the letter-logs,
                # and within the digit-logs subgroup, it maintains the original order
                # (since we don't provide any further sorting keys for digit-logs).
                return (1,)

        # Funciton `sorted` returns a new arrays. The other `.sort()` array method does sorting in place and returns None.
        return sorted(logs, key=get_sort_key)
        #OR
        # Sort logs using sort() function. The key parameter takes a function
        # that extracts sorting keys from the log entries.
        # The logs are sorted according to the keys provided by the get_log_key function.
        # logs.sort(key=get_sort_key)
        # return logs

# Note:
# the first item in tuple determines what comes first. 0 comes before 1.



# Let:
# N be the number of logs in the list.
# M be the maximum length of a single log string.
# Time Complexity: O(M * N log N)
# Sorting: The main operation is sorted(), which uses the Timsort algorithm. Timsort has a time complexity of O(K log K) where K is the number of items being sorted. Here, K is N, so the sorting part is O(N log N) comparisons.
# Key Function and Comparisons: We need to consider the cost of each comparison. A comparison involves running the get_sort_key function and then comparing the resulting keys (tuples).
# log.split(): This takes O(M) time as it may need to scan the entire string.
# Tuple comparison: In the worst case (comparing two letter-logs with identical content), Python needs to compare the content strings and then the identifier strings. This comparison also takes O(M) time.
# Since each of the O(N log N) comparisons can take up to O(M) time, the total time complexity is the product of these two factors.

# Total Time Complexity = O(M * N log N)

# Space Complexity: O(N * M)
# sorted() Output: The sorted() function creates a new list containing the sorted logs. The space required to store this new list is proportional to the total size of the input data, which is O(N * M).
# Keys for Sorting: During the sorting process, Python needs to store the key for each of the N logs. The key for a letter-log is (0, content, identifier). The content and identifier strings are new strings created by the split() operation. In the worst case, the total size of all these keys stored in memory is also O(N * M).
# The space required for the output list and the keys used during sorting are both on the order of O(N * M).

# Total Space Complexity = O(N * M)