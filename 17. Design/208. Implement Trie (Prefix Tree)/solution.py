class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            # if charachter is not in children, then add it
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        # mark the end of the word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        if curr.endOfWord == True:
            return True
        
        return False
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return True

# T:O(n), for all methods
# S: O(1) for search and startsWith
#  S: O(k) for insert, where k is number of new trie nodes created. k is <= m. In worst case k == m, when all new nodes created.

# Important:
# For search and insert methods I could just use the hashmap. It would also give me O(1).
# The power of trie is in the startsWith method that Trie can implement in O(p), where p length of prefix.

