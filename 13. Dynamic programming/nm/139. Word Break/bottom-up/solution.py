# Dynamic programing problem: split a complex problem into smaller ones.
# In this case the smaller problems answer the question: "Can the string up to the i-th character be segmented into a sequence of dictionary words?"

def wordBreak(s, wordDict):
    wordSet = set(wordDict)  # Convert to set for O(1) lookups
    n = len(s)


    dp = [False] * (n + 1)

    print("word length", n)
    print("dp length", len(dp))

    dp[0] = True  # Base case: empty string. It is always possible to segmebt the empty string.
    # With True value we mark that last char in string that up to this point the strng could be broken down into dictionary words.
    print("dp", dp)

   
    for i in range(1, n + 1):  # Iterate over all the charachters of the string. From first ot last char.
        print("============")
        print("--i", i)
        for j in range(i):  # Check all partitions s[j:i]. So from string start(j) to end string char from above(i) 
            print("++j", j)
            print("dp[j]", dp[j])
            print("s[j:i]", s[j:i])
            if dp[j] and s[j:i] in wordSet: #here the dp[j] must be True to ensure that all chars before j can be separated in separate words. This is the same as statement that s[0:j] could be split in other words.
                print("setting the dp to true", i)
                dp[i] = True  # with this True i say that all chars from string TILL char i could be devided in words from dictionary 
                break  # No need to check further if True because we already got the biggest possible substring
    
    print("dp in the end", dp)
    # If the last char is true, it means that the whole string up to this point could be broken down into words from 
    return dp[n]


# T: O(n^3) 
# 1. Outer Loop (for i): This loop runs n times, where n is the length of the string s. This gives us O(n).
# 2. Inner Loop (for j): This loop also runs up to n times in the worst case (when i is close to n). This gives us another O(n).
# 3. String Slicing (s[j:i]): This is the hidden factor. In Python, creating a substring slice is not a free operation. It takes time proportional to the length of the slice. In the worst case, the slice can be of length n. This gives us a third O(n).

# S: O(n+m) , n for wordSet length and m for dp length.


# Example Usage:
s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))  # Output: True



# Intuition
# Imagine s = "applepenapple" and wordDict = ["apple", "pen"].

# The Core Idea
# The main idea is to build a dp array where dp[i] answers the question: "Can the substring from the beginning of s up to index i be broken into words from our dictionary?"

# So, for s = "applepenapple" (length 13), our dp array will have length 14.

# dp[5] will be True because "apple" is in the dictionary.
# dp[8] will be True because "applepen" can be broken into "apple" and "pen".
# The final answer is dp[13], which tells us if the entire string can be broken down.
# Step-by-Step Logic
# dp = [False] * (n + 1)
# We create a boolean array, one element longer than the string. dp[i] corresponds to the substring s[0:i].
# It's initialized to False because we don't yet know if any substring can be formed.
# dp[0] = True (The Base Case)
# This is the most crucial step. dp[0] represents an empty prefix string (""). We set it to True because an empty string can always be "segmented" (by choosing no words).
# This True value acts as the starting point for our logic.
# The Loops: for i ... and for j ...
# The code iterates through the string s one character at a time (the i loop, from 1 to n). For each character i, it tries to answer: "Can we end a valid segment right here?"
# To do that, it looks backward from i (the j loop). It checks every possible "last word" ending at i. This "last word" is the substring s[j:i].
# The Condition: if dp[j] and s[j:i] in wordSet:
# This is the heart of the DP logic. It checks two things for the substring s[j:i]:
# s[j:i] in wordSet: Is this potential "last word" actually a valid word in our dictionary?
# dp[j]: Is the part of the string before this potential last word (s[0:j]) also breakable?
# If both are True, it means we have successfully segmented the string up to index i.
# Example Walkthrough: s = "applepen", wordDict = ["apple", "pen"]
# n = 8, dp array is [F, F, F, F, F, F, F, F, F]
# dp[0] = True -> dp is [T, F, F, F, F, F, F, F, F]
# i = 1 to 4: dp remains False because "a", "ap", "app", "appl" are not in the dictionary.

# i = 5:

# j loops from 0 to 4.
# When j = 0:
# Check s[0:5] which is "apple".
# Condition: dp[0] is True AND "apple" is in the dictionary.
# It's a match! We set dp[5] = True.
# break the inner j loop because we've already confirmed s[0:5] is breakable.
# dp is now [T, F, F, F, F, T, F, F, F]
# i = 6 to 7: No new words are found, dp remains unchanged.

# i = 8:

# j loops from 0 to 7.
# The code checks substrings like "applepen", "pplepen", "plepen", etc.
# When j = 5:
# Check s[5:8] which is "pen".
# Condition: dp[5] is True AND "pen" is in the dictionary.
# It's a match! This means the string before "pen" (s[0:5]) was breakable, and "pen" itself is a valid word. So, the whole string s[0:8] is breakable.
# We set dp[8] = True.
# break the inner j loop.
# dp is now [T, F, F, F, F, T, F, F, T]
# Final Step:

# The loops finish. The function returns dp[n], which is dp[8].
# dp[8] is True, so the function correctly returns True.