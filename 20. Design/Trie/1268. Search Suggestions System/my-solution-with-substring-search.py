class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = set()

class Solution:
    def search(self, trie, word):
        curr_node = trie
        for ch in word:
            if ch not in curr_node.children:
                return

            curr_node = curr_node.children[ch]
        
        return curr_node.indexes

    def get_suggestions(self, products, trie, searchWord):
        searched_indexes = self.search(trie, searchWord)
        if not searched_indexes:
            return []
        res = []
        for idx, val in enumerate(products):
            if idx in searched_indexes:
                res.append(val)
        if len(res) > 3:
            res.sort()
        return res

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #sort products in the beginning to achieve lexicographically minimums. I store only three ids per node.
        products.sort()

        trie = TrieNode()
        curr_node = trie

        # build trie tree
        for idx, product in enumerate(products):
            prefix = 0
            while prefix < len(product) - 1:
                curr_node = trie

                for ch in product[prefix:]:
                    if ch not in curr_node.children:
                        curr_node.children[ch] = TrieNode()
                        curr_node = curr_node.children[ch]
                        # note! save seen index on the actual letter node and not on the parent!
                        curr_node.indexes.add(idx)
                    else:
                        curr_node = curr_node.children[ch]
                        # note! save seen index on the actual letter node and not on the parent!
                        if idx not in curr_node.indexes and len(curr_node.indexes) < 3:
                            curr_node.indexes.add(idx)

                prefix += 1

        # get seatched items
        res = []
        for idx, ch in enumerate(searchWord):
            res.append(self.get_suggestions(products, trie, searchWord[:idx+1])[:3])
        
        return res




