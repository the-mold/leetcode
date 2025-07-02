def gcdOfStrings(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        
        # number of substring repetitions in a string
        n1 = len1 // k
        n2 = len2 // k
        tested_substring = str1[:k]

        return str1 == tested_substring * n1 and str2 == tested_substring * n2

    for i in range(min(len1, len2), 0, -1):   #O(n)
        if valid(i):
            return str1[:i]
    
    return ""

# T: O(n+m)
# S: O(min(n,m))     , I need to keep copy of tested_substring in every itteration