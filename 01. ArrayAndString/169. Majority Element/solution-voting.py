from typing import List

def majority_element(nums: List[int]) -> int:
    """
    Finds the majority element in a list using the Boyer-Moore Voting Algorithm.
    The majority element is the element that appears more than ⌊n / 2⌋ times.

    Args:
        nums: The input list of numbers.

    Returns:
        The majority element.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        count += 1 if num == candidate else -1

    # The problem statement guarantees that a majority element always exists,
    # so the final candidate is the answer. A second pass to verify is not needed.
    return candidate

# T: O(n)
# S: O(1)