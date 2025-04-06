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


# T: O(n^2) , the worst case when s[j:i] is a word in dictionary
# S: O(n+m) , n for wordSet length and m for dp length.


# Example Usage:
s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))  # Output: True
