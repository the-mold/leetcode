def isSubsequence(self, s: str, t: str) -> bool:
    s_list = list(s)
    s_len = len(s_list)
    t_list = list(t)

    lastTestedCharInS = 0

    for i in range(len(t_list)):
        if s_len == lastTestedCharInS:
            break

        if s_list[lastTestedCharInS] == t_list[i]:
            lastTestedCharInS += 1
    
    return s_len == lastTestedCharInS

# T: O(n)
# S: O(n)