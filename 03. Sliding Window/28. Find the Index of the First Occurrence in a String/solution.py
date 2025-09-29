def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)
    
    window_start_idx = 0

    for window_start_idx in range(n - m + 1):
        for i in range(m):
            if haystack[window_start_idx+i] != needle[i]:
                break
            elif i == m - 1:
                return window_start_idx
    
    return -1

strStr("a", "a")
# strStr("mississippi", "issipi")

# T:O(n*m)
# S:O(1)
