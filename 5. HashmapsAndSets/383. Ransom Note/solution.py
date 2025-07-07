def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    freq = {}
    for char in magazine:
        freq[char] = freq.get(char, 0) + 1
    
    for char in ransomNote:
        if char not in freq:
            return False
        
        if freq.get(char, 0) == 0:
            return False

        freq[char] = freq.get(char, 0) - 1
    
    return True

#T:O(n+m)
#S:O(1) becase possible chars that are stored are bounded by the alphabet
