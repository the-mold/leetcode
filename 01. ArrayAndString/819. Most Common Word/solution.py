class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # replace punctuation with empty spaces
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")

        # split by empty spaces
        paragraph_array = paragraph.split(" ")
        
        # make frequency map
        dict_p = {}
        banned_sett = set(banned)
        for word in paragraph_array:
            word = word.lower()
            if word in banned_sett:
                continue
            if not word:
                continue
            dict_p[word] = dict_p.get(word, 0) + 1

        # find max
        max_count = 0
        res = ""
        for key in dict_p:
            if dict_p[key] > max_count:
                res = key
                max_count = dict_p[key]
        
        return res


# Time Complexity: O(N+M).

# It would take O(N) time to process each stage of the pipeline as we built.

# In addition, we built a set out of the list of banned words, which would take O(M) time.

# Hence, the overall time complexity of the algorithm is O(N+M).

# Space Complexity: O(N+M).

# We built a hashmap to count the frequency of each unique word, whose space would be of O(N).

# Similarly, we built a set out of the banned word list, which would consume additional O(M) space.

# Therefore, the overall space complexity of the algorithm is O(N+M).
