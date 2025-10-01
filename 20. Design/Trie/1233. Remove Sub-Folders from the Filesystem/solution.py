class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndFolder = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        ans = []

        # build tree
        for path in folder:
            curr_node = self.root

            folders = path.split("/")

            for folder_name in folders:
                if folder_name == " ":
                    continue

                if folder_name not in curr_node.children:
                    curr_node.children[folder_name] = TrieNode()

                curr_node = curr_node.children[folder_name]

            curr_node.isEndFolder = True


        # check each folder. Terminate if on the way you see that there was alread isEndFolder = True.
        # this way you know that current folder is subfolder.
        for path in folder:
            curr_node = self.root
            folders = path.split("/")
            is_subfolder = False

            for idx, folder_name in enumerate(folders):
                if folder_name == " ":
                    continue

                next_node = curr_node.children[folder_name]
                # Check if the current folder path is a subfolder of an existing folder
                if next_node.isEndFolder and idx != len(folders) - 1:
                    is_subfolder = True
                    break  # Found a subfolder

                curr_node = next_node

            if not is_subfolder:
                ans.append(path)

        return ans
        
        
# Time complexity: O(N×L)
# For each folder path in folderPaths, the algorithm parses the path and inserts it into the Trie. Parsing each path takes O(L) time.
# For each segment, checking and inserting into Trie’s map also takes O(L) time on average due to hash table operations (insertions and lookups in the map). Therefore, building the Trie for all N paths results in a total time complexity of O(N×L).
# For each folder path, the algorithm traverses the Trie to check if it is a subfolder. Again, parsing the path takes O(L), and each lookup in the map takes O(1) on average. Therefore, checking all N folder paths also requires O(N×L) time.
# Overall, both the Trie-building and subfolder-checking phases have a time complexity of O(N×L), so the total time complexity is: O(N×L)

# Space complexity: O(N×L)
# Each folder path can create up to L nodes in the Trie, depending on the path depth. In the worst case, if all folder paths are unique, we would end up storing all N×L segments. Therefore, the space required for the Trie structure is O(N×L).
# The result array stores up to N folder paths, so its space requirement is O(N). Intermediate variables like iss and string use O(L) space for each folder path.
# Since the Trie is the most space-consuming data structure in this solution, the overall space complexity is: O(N×L)
