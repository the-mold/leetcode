def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    if n == 0:
        return []

    left = [0] * n
    right = [0] * n
    ans = [0] * n
    
    left[0] = 1
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    
    right[n-1] = 1
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
        
    for i in range(n):
        ans[i] = left[i] * right[i]
        
    return ans

#Intuition
#For each position calculate product of all items to the left(left array).
#Then for each position calculate product of all items to the right(right array).
# Then calculate product of both arrays to get final result.

# Example:
# For input [1,2,3,4]:
# left:  [1, 1, 2, 6]    // Products of all elements to the left
# right: [24, 12, 4, 1]  // Products of all elements to the right
# ans:   [24, 12, 8, 6]  // left[i] * right[i] at each position
