class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        # if you split "/a/b/c" you get ['', 'a', 'b', 'c']
        folders = path.split("/")

        curr_node = self.root
        # loop through all folders except for the last one
        for i in range(len(folders) - 1):
            folder = folders[i]
            if not folder:
                continue

            # check if all parent nodes exist in trie already
            if folder not in curr_node.children:
                return False
            curr_node = curr_node.children[folder]
        
        # final folder to be added
        final_folder = folders[-1]
        if final_folder in curr_node.children:
            return False # Path already exists

        newNode = TrieNode()
        newNode.value = value
        curr_node.children[final_folder] = newNode

        return True

    def get(self, path: str) -> int:
      # if you split "/a/b/c" you get ['', 'a', 'b', 'c']
        folders = path.split("/")
        curr_node = self.root

        for folder_name in folders:
            if not folder_name:
                continue

            if folder_name not in curr_node.children:
                return -1
            
            curr_node = curr_node.children[folder_name]

        return curr_node.value

        

