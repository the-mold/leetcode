def generate_pascals_triangle_dp(numRows):
    # Initialize a 2D DP array filled with zeros
    dp = [[0 for _ in range(numRows)] for _ in range(numRows)]
    
    # Initialize result list to store each row
    result = []
    
    for i in range(numRows):
        # Create current row to append to result
        current_row = []
        
        #here we control how many items are placed in each row.
        # If i == 0,the we place only 1 element [1],
        # if i == 1, we place two elements [1,1] etc.
        for j in range(i + 1): 
            # Base cases: first and last elements in each row are 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # DP relation: each element is sum of two elements from previous row
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
            current_row.append(dp[i][j])
        
        result.append(current_row)
    
    return result


# Time Complexity: O(n²)
# The outer loop runs numRows times
# The inner loop runs up to i+1 times for each row i
# Total number of operations: 1 + 2 + ... + numRows = numRows*(numRows+1)/2, which simplifies to O(n²)
# Each operation inside the loops is constant time O(1)

# Space Complexity: O(n²)
# We're using a full numRows × numRows DP array, which takes O(n²) space
# Note that we could optimize this to O(n) space by only keeping track of the previous row, but the current implementation uses O(n²)
# We also store the result list which contains all elements of Pascal's triangle, taking another O(n²) space