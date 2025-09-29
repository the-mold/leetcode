def closeStrings(self, word1: str, word2: str) -> bool:
    # Prep: create frequency map
    freq_map1 = {}
    for char in word1:
        freq_map1[char] = freq_map1.get(char, 0) + 1
    
    freq_map2 = {}
    for char in word2:
        freq_map2[char] = freq_map2.get(char, 0) + 1

    # 1. strings must have the same chars
    if set(word1) != set(word2):
        return False

    # 2. Frequency distribution must be the same. This is to meed the second condition: all a's turn into b's, and all b's turn into a's. Number of SOME letters must be the same. If there are 3 As in nums1, then there must be 3 Bs in nums2.
    freq1 = sorted(freq_map1.values())
    freq2 = sorted(freq_map2.values())
    if freq1 != freq2:
        return False

    return True

#T:O(n + m + k log k) => k(sorting) is bounded to alphabet, overal complexity is => O(n+m)
#S:O(k) => O(1), because k is bounded by alphabet charachters.