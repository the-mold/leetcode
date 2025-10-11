class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        all_letters = set(s)
        max_length = 0

        for letter in all_letters:
            target_letter_count = 0
            start = 0

            for end in range(len(s)): #n
                if letter == s[end]:
                    target_letter_count += 1

                # shrink window from left till window is valid
                while not self._window_is_valid(start, end, target_letter_count, k):
                    if letter == s[start]:
                        target_letter_count -= 1
                    start += 1

                max_length = max(max_length, end - start + 1)
        
        return max_length
    
    def _window_is_valid(self, start, end, target_letter_count, k):
        return end - start + 1 - target_letter_count <= k

# T:O(nm), where n length of string and m number of unique charachters
# S:O(m) for set