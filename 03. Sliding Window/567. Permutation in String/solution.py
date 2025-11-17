class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord("a")] += 1

        for i in range(n2):
            # for all cases when window is more than the length of s1, start removing in each itteration a char on the left to keep window of fixed size.
            if i >= n1:
                s2_count[ord(s2[i-n1]) - ord("a")] -= 1

            s2_count[ord(s2[i]) - ord("a")] += 1

            if s1_count == s2_count:
                return True
        
        return False

#T:O(n1 + n2) => O(n)
#S:O(n)
