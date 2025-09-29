# A dataclass is a simple way to create a class for storing data.
# This is our blueprint for each node in the trie.
from dataclasses import dataclass, field
from typing import Dict, Set, List

@dataclass
class TrieNode:
    """
    Represents a single node in our character-level trie.
    """
    # 'children' is a dictionary that maps a character to another TrieNode.
    # For example: {'a': TrieNode(...), 'b': TrieNode(...)}
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    
    # 'doc_ids' is a set that will store the integer IDs of all documents
    # that contain the character sequence leading to this node.
    # We use a set for two reasons:
    # 1. It automatically handles duplicates (a doc ID can only be in a set once).
    # 2. Checking if an ID is already in the set is very fast.
    doc_ids: Set[int] = field(default_factory=set)

class SimpleSearchEngine:
    """
    A search engine using a character-level suffix trie.
    """
    def __init__(self):
        # The entire trie starts with a single empty root node.
        self.root = TrieNode()
        
        # This list will hold the original, unaltered documents.
        # The index of a document in this list will be its ID.
        self.documents: List[str] = []

    def add_document(self, doc_text: str):
        """
        Adds a document to the search engine's index.
        """
        # The ID for this new document is simply its index in our documents list.
        doc_id = len(self.documents)
        self.documents.append(doc_text)
        
        # As requested, we work with lowercase text to make searches case-insensitive.
        text = doc_text.lower()

        # --- This is the most important part of building a SUFFIX trie ---
        # We must loop through the document starting from every possible character.
        # This ensures that we can find phrases that appear anywhere, not just at the beginning.
        for i in range(len(text)):
            # For each starting position 'i', we start our traversal from the root.
            current_node = self.root
            
            # Get the suffix of the text starting from index 'i'.
            # Example: if text is "cat", the suffixes are "cat", "at", "t".
            suffix = text[i:]
            
            # Now, we add this suffix to the trie, character by character.
            for char in suffix:
                # If the character is not already a child of the current node,
                # we create a new node for it.
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                
                # Move down to the child node.
                current_node = current_node.children[char]
                
                # We've now processed this character. We record that the current
                # document (doc_id) contains the phrase leading to this node.
                current_node.doc_ids.add(doc_id)

    def search(self, phrase: str) -> List[str]:
        """
        Searches for an exact phrase and returns a list of matching documents.
        """
        # Also make the search phrase lowercase to match the indexed text.
        search_phrase = phrase.lower()
        
        # Start the search traversal from the root of the trie.
        current_node = self.root
        
        # Follow the path in the trie corresponding to the search phrase.
        for char in search_phrase:
            # If at any point the next character is not in the children,
            # it means the phrase does not exist in our index.
            if char not in current_node.children:
                # So, we can stop and return an empty list.
                return []
            
            # Otherwise, move down to the next node in the path.
            current_node = current_node.children[char]
            
        # If we successfully finish the loop, 'current_node' is the node
        # that represents the end of our search phrase.
        
        # The 'doc_ids' at this final node tell us every document
        # that contains the search phrase.
        matching_ids = current_node.doc_ids
        
        # Finally, we retrieve the original documents using their IDs.
        # We sort the IDs to ensure the results are always in a consistent order.
        return [self.documents[doc_id] for doc_id in sorted(list(matching_ids))]

# --- Demonstration ---
if __name__ == "__main__":
    # 1. Create an instance of our search engine.
    engine = SimpleSearchEngine()

    # 2. The sample documents to be indexed.
    sample_docs = [
        "the quick brown fox",
        "the slow brown cow",
        "to be or not to be that is the question",
        "bar foo bar barfoo",
    ]

    # 3. Add each document to the engine.
    print("Indexing documents...")
    for doc in sample_docs:
        engine.add_document(doc)
    print("Indexing complete.\n")

    # 4. The search phrases to test.
    search_queries = [
        "brown",
        "slow brown",
        "the cow",
        "bar bar",
        "o",
    ]

    # 5. Run the searches and print the results.
    for phrase in search_queries:
        results = engine.search(phrase)
        print(f'Searching for: "{phrase}"')
        print(f'  => Found in: {results}\n')