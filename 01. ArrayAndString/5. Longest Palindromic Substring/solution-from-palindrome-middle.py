class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_count = 0
        ans = ""

        for i in range(len(s)): # loop over all letters in string and assume it is middle letter of a palindrome.
            # odd length
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > ans_count:
                    ans_count = curr_length
                    ans = s[l:r+1]
                l -= 1
                r += 1

            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > ans_count:
                    ans_count = curr_length
                    ans = s[l:r+1]
                l -= 1
                r += 1

        return ans

# Time complexity: O(n**2)
# There are 2n−1=O(n) centers. For each center, we call expand, which costs up to O(n).
# Although the time complexity is the same as in the DP approach, the average/practical runtime of the algorithm is much faster. This is because most centers will not produce long palindromes, so most of the O(n) calls to expand will cost far less than n iterations.
# The worst case scenario is when every character in the string is the same.

# Space complexity: O(1)
# We don't use any extra space other than a few integers. This is a big improvement on the DP approach.
