class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        # Sort the target string s1 once.
        s1_sorted = "".join(sorted(s1))

        # Iterate through all windows of size n1 in s2.
        for i in range(n2 - n1 + 1):
            # Get the substring (window) from s2.
            substring_s2 = s2[i : i + n1]
            
            # Sort the substring FOR EVERY window.
            substring_s2_sorted = "".join(sorted(substring_s2))
            
            # Compare the sorted strings.
            if s1_sorted == substring_s2_sorted:
                return True
        
        return False

# T:O(N * m log m)
# S:O(m)
