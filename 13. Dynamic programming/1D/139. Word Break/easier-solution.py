class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # state - bool if some word from wordDict ends here given that i - len(word) is also true

        # ds
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                # check if i could be built with the word
                if i >= len(word) - 1:
                    # proceed with word if
                    # this is the first word in string OR previous char ended with a valid word(dp[i - len(word)] == True)
                    if i == len(word) - 1 or dp[i - len(word)] == True:
                        if s[i - len(word) + 1: i + 1] == word: #check if word is the same
                            dp[i] = True
                            break

        return dp[-1]

# [l e e t c o d e]
# [F F F F F F F F]
# s = "leetcode"
# wordDict = ["leet","code"]
