from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # Store at most 3 lexicographically smallest products

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products to ensure lexicographic order
        products.sort()
        
        # Build trie
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                
                # Add product to suggestions if we have less than 3
                # Since products are sorted, first 3 are lexicographically smallest
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        
        # Search for suggestions
        result = []
        node = root
        
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions[:])  # Copy the list
            else:
                # No more matches possible, all remaining will be empty
                node = None
                result.append([])
        
        return result


# Complexity Analysis

# Time complexity : O(M) to build the trie where M is total number of characters in products For each prefix we find its representative node in O(len(prefix)) and dfs to find at most 3 words which is an O(1) operation. Thus the overall complexity is dominated by the time required to build the trie.

# In Java there is an additional complexity of O(m 
# 2
#  ) due to Strings being immutable, here m is the length of searchWord.
# Space complexity : O(26n)=O(n). Here n is the number of nodes in the trie. 26 is the alphabet size.
# Space required for output is O(m) where m is the length of the search word.





# Test with examples
solution = Solution()

# Example 1
products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord1 = "mouse"
print(solution.suggestedProducts(products1, searchWord1))
# Expected: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

# Example 2
products2 = ["havana"]
searchWord2 = "havana"
print(solution.suggestedProducts(products2, searchWord2))
# Expected: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]