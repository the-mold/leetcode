def rob_with_dp_array(nums):
    """
    Calculates the maximum amount of money that can be robbed from a street of houses
    without robbing two adjacent houses, using a DP array.

    Args:
        nums: A list of integers representing the money in each house.

    Returns:
        The maximum amount of money that can be robbed.
    """
    n = len(nums)

    # Handle edge cases where the list is empty or has only one house
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # dp[i] will store the maximum money that can be robbed from houses 0 to i.
    dp = [0] * n

    # Base Cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Fill the rest of the dp array using the recurrence relation
    for i in range(2, n):
        # For house i, we have two choices:
        # 1. Rob house i: The total is nums[i] + dp[i-2] (money from current + max from 2 houses ago)
        # 2. Don't rob house i: The total is dp[i-1] (the max we had up to the previous house)
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
    # The final element in the dp array contains the maximum amount for the whole street
    return dp[n-1]

# --- Examples ---
print(f"Input: [1, 2, 3, 1], Output: {rob_with_dp_array([1, 2, 3, 1])}")
print(f"Input: [2, 7, 9, 3, 1], Output: {rob_with_dp_array([2, 7, 9, 3, 1])}")