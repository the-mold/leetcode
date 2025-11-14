def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    if n == 0:
        return []

    answer = [1] * n

    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]

    suffix_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix_product   # multiply here because there is already value from prefix. You cannot just overwrite it.
        suffix_product *= nums[i]
    
    return answer


# T:O(n)
# S:O(1), the solution has O(n) but it is expected by the problem. O(1) means that my solution does not use any additional space.

