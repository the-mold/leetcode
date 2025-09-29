class Solution:
    def is_palindrome(self, s):
        s = s.lower()
        return s == s[::-1] # compare string and its reverse

    def longestPalindrome(self, s: str) -> str:
        ans_longest_palindrom = ""
        input_string_length = len(s)

        if not s or len(s) == 1:
            return s

        for l in range(input_string_length):
            for r in range(l, input_string_length):
                print("r", r)
                tested_string = s[l:r+1]
                if self.is_palindrome(tested_string):
                    if len(tested_string) > len(ans_longest_palindrom):
                        ans_longest_palindrom = tested_string

        return ans_longest_palindrom

# Complexity O(n^3): n for palindrome check and n^2 for two loops. Together n^3
