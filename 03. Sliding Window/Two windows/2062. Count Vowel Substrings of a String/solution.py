class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        return self.count_at_most_k_vowels(word, 5) - self.count_at_most_k_vowels(word, 4)
            
    def count_at_most_k_vowels(self, word, k):
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        l = 0
        freq_map = collections.defaultdict(int)

        for r in range(len(word)):
            # If consonant, reset window
            if word[r] not in vowels:
                freq_map.clear()
                l = r + 1
                continue

            freq_map[word[r]] += 1

            # shrink window if thre are more than k vowels
            while len(freq_map) > k:
                freq_map[word[l]] -= 1
                if freq_map[word[l]] == 0:
                    del freq_map[word[l]]
                l += 1

            # all substrings from l to r are valid
            count += r - l + 1

        return count

# T:O(n)
# S:O(1), because dict hast max k keys. It is fixed size, therefore O(1)

