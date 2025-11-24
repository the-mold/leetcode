# Intuition: for each word in queue generate ALL possible words from it(by substituting each char through an alphabet letter).
# If a new word is in wordList, then add it to the queue. VERY INEFFICIENT!

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Step 1: Pre-computation and Setup
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Queue for BFS: stores (word, current_path_length)
        queue = deque([(beginWord, 1)])
        
        # Visited set to avoid cycles and redundant processing
        visited = {beginWord}

        # Step 2: BFS Loop
        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            # Step 3: Find Neighbors by generating all possible one-letter mutations
            for i in range(len(current_word)):
                # Convert word to list to modify characters
                word_chars = list(current_word)
                
                # Try replacing the character at index `i` with every letter 'a' through 'z'
                for char_code in range(ord('a'), ord('z') + 1):
                    original_char = word_chars[i]
                    new_char = chr(char_code)
                    
                    # Skip if it's the same character
                    if original_char == new_char:
                        continue

                    word_chars[i] = new_char
                    new_word = "".join(word_chars)

                    # Step 4: Check and Enqueue the new word
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))
                
                # Backtrack: restore the original character for the next position's mutations
                word_chars[i] = original_char

        # Step 5: No path found
        return 0


# Key Variables
# N: The number of words in wordList.
# M: The length of each word (since all words have the same length).
# A: The size of the alphabet (which is 26, a constant).

# Time Complexity: O(N * M²)*
# Let's break down where this comes from. The main work happens inside the while loop, which processes each word in the wordList at most once.

# Outer while loop:
# In the worst case, the BFS will visit every single word in the wordList that is reachable from beginWord. This means the loop will run at most N times.
# Inner "Find Neighbors" loop (for each word):
# For each current_word dequeued, you have a loop that runs M times (the length of the word).
# Inside that, you have another loop that runs A times (26 times for the alphabet).
# Inside that, you create a new_word. Creating a string from a list of characters takes O(M) time.
# So, for a single word, the cost of generating all its neighbors is M * A * M = O(A * M²). Since A is a constant (26), this simplifies to O(M²).
# Total Time:
# We process up to N words.
# For each word, we do O(M²) work to find its neighbors.
# Therefore, the total time complexity is N * O(M²) = O(N * M²).*
# Initial Setup:

# word_set = set(wordList): This takes O(N * M) time because it has to process N words of length M.
# This setup cost is less than the main loop's complexity, so it doesn't change the overall result.*
# Conclusion: The dominant factor is generating and checking all possible one-letter mutations for every word visited.

# Space Complexity: O(N * M)*
# The space complexity is determined by the data structures used to store the words.

# word_set:
# This set stores all N words from the wordList.
# Each word has a length of M.
# Space: O(N * M)
# queue:
# In the worst case, the queue could hold all N words at once (for example, if beginWord can transform into every word in wordList in one step).
# Space: O(N * M)
# visited:
# This set also stores up to N words.
# Space: O(N * M)*
# Conclusion: The space required is proportional to the number of words multiplied by their length, making the final space complexity O(N * M).*