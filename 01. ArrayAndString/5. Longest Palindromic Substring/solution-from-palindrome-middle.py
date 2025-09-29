class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_longest_palindrom = s[0]
        ans_longest_palindrom_length = 1
        input_string_length = len(s)

        for i in range(input_string_length): # loop over all letters in string and assume it is middle letter of a palindrome.
       
            # test for odd length palindromes
            l, r = i, i
            while l >= 0 and r < input_string_length and s[l] == s[r]:
                palindrome_length = (r - l) + 1
                if palindrome_length > ans_longest_palindrom_length:
                    ans_longest_palindrom_length = palindrome_length
                    ans_longest_palindrom = s[l:r+1]
                l -= 1
                r += 1
    
            # test for even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < input_string_length and s[l] == s[r]:
                palindrome_length = (r - l) + 1
                if palindrome_length > ans_longest_palindrom_length:
                    ans_longest_palindrom_length = palindrome_length
                    ans_longest_palindrom = s[l:r+1]
                l -= 1
                r += 1

        return ans_longest_palindrom

