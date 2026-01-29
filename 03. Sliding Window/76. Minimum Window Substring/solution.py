class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains all characters of t.

        This solution uses the sliding window algorithm with basic dictionaries.

        1.  It first creates a frequency map of characters in `t` using a standard dict.
        2.  It then uses two pointers, `left` and `right`, to define a sliding window in `s`.
        3.  The `right` pointer expands the window. As it does, we track the characters
            from `t` that are now satisfied within our window.
        4.  Once the window contains all required characters from `t`, we try to shrink
            it from the left by moving the `left` pointer. This helps us find the
            smallest possible valid window.
        5.  We keep track of the minimum window found so far and return it after
            checking all possibilities.
        """
        if not t or not s:
            return ""

        # Dictionary to store the frequency of characters in t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        required = len(dict_t)

        # Sliding window pointers
        left, right = 0, 0

        # `formed` is used to track how many unique characters in t
        # are currently satisfied in the window.
        formed = 0

        # Dictionary to store the frequency of characters in the current window
        window_counts = {}

        # Variables to store the result:
        # (window length, left pointer, right pointer)
        ans = float("inf"), None, None

        while right < len(s):
            # Add one character from the right to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character in the window
            # matches its frequency in t, increment `formed`.
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window from the left
            while left <= right and formed == required:
                # Update the minimum window found so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove the character at the left of the window
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If the removed character was required and its count
                # in the window drops below the required count, decrement `formed`.
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                
                # Move the left pointer to the right to shrink the window
                left += 1
            
            # Expand the window by moving the right pointer
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    

# Time Complexity: O(M + N)
# Building the Frequency Map (O(N)): First, we iterate through the string t once to create the dict_t frequency map. This takes time proportional to the length of t, so it's O(N).
# Sliding Window (O(M)): The core of the algorithm uses two pointers, left and right.
# The right pointer moves from the start to the end of string s exactly once.
# The left pointer also moves from the start to the end of s at most once.
# Even though there's a nested while loop, each character of s is processed by the right pointer once and by the left pointer once. This means we are effectively making a single pass over s. Therefore, this part of the algorithm is O(M).
# Combining these two steps, the total time complexity is O(N) + O(M) = O(M + N). 

#S: O(∣S∣+∣T∣). ∣S∣ when the window_counts is equal to the entire string S. ∣T∣ when T has all unique characters, hence dict_t has all unique chars.
