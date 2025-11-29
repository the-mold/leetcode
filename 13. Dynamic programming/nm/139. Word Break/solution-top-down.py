class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._wordBreak(s, wordDict, 0, {})

    def _wordBreak(self, s, wordDict, idx, memo):
        if idx in memo:
            return memo[idx]

        if idx == len(s):
            return True

        for word in wordDict:
            # if string starts with the word at given index
            if s.startswith(word, idx):
                if self._wordBreak(s, wordDict, idx + len(word), memo):
                    memo[idx] = True
                    return True

        memo[idx] = False
        return False

#s = string length
#n = number of words

#T:O(ns)
#S:O(s)
