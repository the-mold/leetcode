def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict_w = {}
    for word in strs:
        count = [0] * 26
        for char in word:
            position_a = ord("a")
            position_char = ord(char)
            count[position_char - position_a] += 1
        
        dict_w.setdefault(tuple(count), []).append(word)
    
    return list(dict_w.values())


groupAnagrams(["eat","tea","tan","ate","nat","bat"])

#T:O(n*k + n*a), where a is size of charset or alphabet
#S:O(n*k + n*a)