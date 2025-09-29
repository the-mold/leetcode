def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = []
    checked_words = {}
    for idx, word in enumerate(strs):
        if word in checked_words:
            continue

        word_group = [word]
        checked_words[word] = True

        for i in range(idx+1, len(strs)):
            candidate = strs[i]
            if candidate in checked_words:
                continue

            dict_w = {}
            for char in word:
                dict_w[char] = dict_w.get(char, 0) + 1
            required = len(word)


            for letter in candidate:
                if letter in dict_w and dict_w[letter] > 0:
                    dict_w[letter] -= 1
                    required -= 1
                else:
                    break   

            if required == 0:
                word_group.append(candidate)
                checked_words[candidate] = True
        
        res.append(word_group)
    
    return res
        

groupAnagrams(["eat","tea","tan","ate","nat","bat"])