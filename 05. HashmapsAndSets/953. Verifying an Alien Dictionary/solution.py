class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create letter_idx_dict
        letter_idx_dict = collections.defaultdict(int)
        for idx, char in enumerate(order):
            letter_idx_dict[char] = idx

        n = len(words)
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]

            min_length = min(len(w1), len(w2))
            # edge case: return false because longer word (that includes shorter) comes before shorter 
            #eg. ["apple", "app"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return False
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    if letter_idx_dict[w1[j]] > letter_idx_dict[w2[j]]:
                        return False
                    break #important! compare only the first char that differs

        return True
      
# Key Variables
# C: The total number of characters in all words combined.
# N: The number of words in the words list.
# M: The maximum length of any single word in the words list.
# A: The length of the order string (the size of the alphabet, which is a constant, typically 26).


# Time Complexity: O(C)
# The overall time complexity is linear with respect to the total number of characters in the input.

# Building the Character Map (O(A) or O(1)):
# for idx, char in enumerate(order):
#     letter_idx_dict[char] = idx
# This loop runs once for each character in the order string. Since the alphabet size A is fixed and small (e.g., 26), this step is considered constant time, or O(1).
# Comparing Adjacent Words (O(C)):
# for i in range(n-1):
#     w1 = words[i]
#     w2 = words[i+1]
#     # ... comparisons ...
# The main loop iterates through N-1 pairs of adjacent words.
# For each pair (w1, w2), you perform character-by-character comparisons. Crucially, you break as soon as you find the first differing character.
# This means that each character in the entire input list is visited at most once across all comparisons. For example, in ["apple", "apply"], you compare a, p, p, l and then e vs y, and then you stop. The y is never compared again.
# The w1.startswith(w2) check also takes time proportional to the length of the words being compared, which contributes to this total character count.
# Therefore, the total work is proportional to the sum of the lengths of all words, which is C.
# Conclusion: The dominant factor is the character comparison loop, making the final time complexity O(C).

# (Note: This is often also written as O(N * M), but O(C) is a tighter and more accurate bound, as you don't always compare up to the maximum length M for every pair of words.)*


# Space Complexity: O(A) or O(1)
# The space complexity is constant because it only depends on the size of the alphabet, not the size of the input words.

# letter_idx_dict:
# python
# letter_idx_dict = collections.defaultdict(int)
# This dictionary stores a mapping for each character in the alien alphabet.
# The number of entries in this dictionary is equal to the length of the order string, which is A.
# Since A is a constant (e.g., 26), the space required is constant.
# Conclusion: The space complexity is O(A), which simplifies to O(1) because the alphabet size does not grow with the input words.