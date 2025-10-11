class Solution:
    def backtracking(self, word, current_word, index, abbreviated_count):
        if index == len(word):
            # If the length of the last abbreviated substring is 0, add an empty string.
            if abbreviated_count > 0:
                current_word += str(abbreviated_count)
            self.res.append(current_word)
            return

        # Option 1: Keep the current character.
        self.backtracking(
            word,
            current_word
            + (str(abbreviated_count) if abbreviated_count > 0 else "")
            + word[index],
            index + 1,
            0,
        )

        # Option 2: Abbreviate the current character.
        self.backtracking(
            word, 
            current_word, 
            index + 1, 
            abbreviated_count + 1
        )

    def generateAbbreviations(self, word: str) -> List[str]:
        self.res = []
        self.n = len(word)
        self.backtracking(word, "", 0, 0)
        return self.res
  
      
# Complexity Analysis
# Here, N is the length of the string word.

# Time complexity: O(N×2**N).

# Each of the N characters in the string word has two choices that we will make until we do it for all the characters. Also, for each string produced, we are appending the abbreviatedString during the process which adds another O(N) time. Since we are going to generate 2**N strings, therefore the time complexity is equal to O(2**N).

# Space complexity: O(N).

# The space used to store the output is generally not considered part of the space complexity. Thus, the only space required is the stack space, the maximum number of active function calls in the stack will be equal to N one for each character in the string word. Hence, the space complexity is equal to O(N).



# Intuition
# We are given a string word of N lowercase English letters. Our task is to choose any number of non-overlapping and non-adjacent substrings from the string and replace them with their length, resulting in an abbreviated string of the original one.

# For example, given the string abcde, we can choose substrings bc and e, replacing bc with 2 and e with 1, resulting in the abbreviated string a2d1. Note that substrings like bc and cd are invalid because they are adjacent, and substrings like abc and cd are invalid because they overlap.

# An important observation is that the length of the string word will be less than 15. To generate all possible abbreviated strings, we need to explore all options. Each character in word can either be part of an abbreviated substring or remain as a separate character. We will explore both options for each character and store the resulting strings in a list.

# For each character, the first option is to keep it as part of the current string without abbreviation. The second option is to abbreviate it. We track three things: the current string being constructed (currWord), the current index in word (index), and the length of the current substring being abbreviated (abbreviatedCount).

# When we choose to abbreviate a character, we increment the abbreviatedCount by 1 and move to the next index. When we choose not to abbreviate, we add the abbreviatedCount to currWord (since the current substring ends), then add the character word[index] to currWord, and reset abbreviatedCount to 0.

# After iterating over all characters in word, we add the final abbreviatedCount to currWord and store the resulting string in a list of all possible abbreviations.

# Algorithm
# Initialize an empty list of strings abbreviations.

# Define the method storeAbbreviations that has three parameters to track currWord, index, and abbreviatedCount. Do the following:

# If the index is equal to the word size, store the abbreviated integer corresponding to the last substring to currWord and then store it in the list abbreviations.
# Define the string abbreviatedString as the abbreviatedCount in the form of a string or an empty string if the integer is 0.
# Recursively call the method when we choose not to abbreviate the current character with index = index + 1, abbreviatedCount = 0, add theabbreviatedString and word[index] to currWord.
# When we choose to abbreviate the current character, make a recursive call with index = index + 1, abbreviatedCount = abbreviatedCount + 1.
# Call the method storeAbbreviations with index = 0 and abbreviatedCount = 0.

# Return abbreviations.

