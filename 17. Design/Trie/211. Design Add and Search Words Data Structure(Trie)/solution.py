class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def search_node(word, node):
            for idx, ch in enumerate(word):
                if ch not in node.children:
                    if ch == ".":
                        for child_key in node.children:
                            if search_node(word[idx+1:], node.children[child_key]):
                                return True

                    return False
                else:
                    node = node.children[ch]
                
            return node.endOfWord

        return search_node(word, self.root)

# Complexity

# addWord:
# Time complexity: O(M), where M is the key length. At each step, we either examine or create a node in the trie. That takes only M operations.
# Space complexity: O(M). In the worst-case newly inserted key doesn't share a prefix with the keys already inserted in the trie. We have to add M new nodes, which takes O(M) space.

# search:
# Time complexity: O(M) for the "well-defined" words without dots, where M is the key length, and N is a number of keys, and O(N⋅26**M) for the "undefined" words. That corresponds to the worst-case situation of searching an undefined word  
# M times which is one character longer than all inserted keys.
# Space complexity: O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words, to keep the recursion stack.
