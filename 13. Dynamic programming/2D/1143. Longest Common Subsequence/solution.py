def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Calculates the length of the longest common subsequence of two strings
    using dynamic programming.

    Args:
      text1: The first string.
      text2: The second string.

    Returns:
      The length of the longest common subsequence.
    """
    m = len(text1)
    n = len(text2)

    # Create a DP table with dimensions (m+1) x (n+1) and initialize with 0s.
    # dp[i][j] will store the length of the LCS of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table using the state transition logic
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, extend the common subsequence
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            # If characters don't match, take the max from the previous states
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value at the bottom-right corner of the table is the result
    return dp[m][n]

# T:O(n*m)
# S:O(n*m)


# Intuition
# The problem asks for the length of the longest common subsequence (LCS) between two strings, text1 and text2. We can solve this efficiently using a 2D DP table.

# Let dp[i][j] be the length of the longest common subsequence of the prefix of text1 of length i (i.e., text1[0...i-1]) and the prefix of text2 of length j (i.e., text2[0...j-1]).

# Our goal is to find dp[m][n], where m is the length of text1 and n is the length of text2.

# State Transition Recurrence
# We can define the dp[i][j] based on the following logic:

# If the characters match (text1[i-1] == text2[j-1]): The last characters of the current prefixes are the same. This character must be part of the LCS. So, the length of the LCS is 1 plus the length of the LCS of the strings without these last characters. dp[i][j] = 1 + dp[i-1][j-1]
# If the characters do not match (text1[i-1] != text2[j-1]): The last characters are different. The LCS must be the longer of the two possibilities:
# LCS of text1[0...i-2] and text2[0...j-1] (which is dp[i-1][j]).
# LCS of text1[0...i-1] and text2[0...j-2] (which is dp[i][j-1]). So, we take the maximum of these two values. dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Base Case
# The base cases are the first row and first column of our DP table. If one of the strings is empty, the length of the LCS is 0. Therefore, dp[0][j] = 0 for all j, and dp[i][0] = 0 for all i.