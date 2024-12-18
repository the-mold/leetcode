# Explanation: https://www.youtube.com/watch?v=FCbOzdHKW18

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        max_unique_string_length = 0
        inpurt_string_length = len(s)
        sett = set()

        for rightPointer in range(inpurt_string_length):
            
            #this while loop ensures that letters in sett are all unique. 
            # Before we move rightPointer further right, make sure that sett is valid
            # by moving leftPointer to the right, if needed. 
            while s[rightPointer] in sett: 
                sett.remove(s[leftPointer])
                leftPointer += 1  #move left pointer to the right
            
            unique_string_length = (rightPointer - leftPointer) + 1
            max_unique_string_length = max(max_unique_string_length, unique_string_length)
            sett.add(s[rightPointer])

        return max_unique_string_length


# Complexity is O(n) even though it looks like there are two loops. 
# The first and the second loop will run at most n times, therefore, O(n).
