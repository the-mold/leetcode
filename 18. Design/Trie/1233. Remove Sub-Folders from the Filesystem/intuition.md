Intuition
A Trie is well-suited for this problem because it allows us to build folder paths incrementally, marking endpoints where folders end. With this structure, any folder that tries to extend beyond an endpoint can be identified as a sub-folder.

We start with an empty Trie and insert folder paths by splitting each path into its components (e.g., "/a/b/c" becomes ["a", "b", "c"]). As we insert each part, we check if we’ve reached an endpoint in the Trie. If so, we can skip the current folder as it’s a sub-folder. Otherwise, we continue inserting the remaining parts. At the end of each path, we mark it as an endpoint.

This way, any future folder that follows an existing path will encounter the endpoint, confirming it as a sub-folder. This is extremely effective for handling deeply nested folder structures.

