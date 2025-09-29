from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    # Take the first word as a reference
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Check if this character matches in all strings
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]

    return strs[0]  # If we go through everything, return full first string

# Example usage
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print(longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
