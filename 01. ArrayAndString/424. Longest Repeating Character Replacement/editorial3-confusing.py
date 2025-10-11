class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # move the start pointer towards right if the current
            # window is invalid
            is_valid = (end + 1 - start - max_frequency <= k)
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end + 1 - start

        return longest_substring_length


# Complexity Analysis
# If there are n characters in the given string.
# Time complexity: O(n). In this approach, we access each index of the string at most two times. When it is added to the sliding window, and when it is removed from the sliding window. The sliding window always moves forward. In each step, we update the frequency map, maxFrequency, and check for validity, they are all constant-time operations. To sum up, the time complexity is proportional to the number of characters in the string - O(n).
# Space complexity: O(m). Similar to the previous approaches, this approach requires an auxiliary frequency map. The maximum number of keys in the map equals the number of unique characters in the string. If there are m unique characters, then the memory required is proportional to m. So the space complexity is O(m). Considering uppercase English letters only, m=26.
