def hamming_weight(n: int) -> int:
    """
    Calculates the number of set bits (Hamming weight) in a positive integer.

    This implementation uses Python's built-in `bin()` function to convert the
    integer to its binary string representation and then counts the occurrences of '1'.

    Args:
        n: A positive integer.

    Returns:
        The number of set bits in the binary representation of n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return bin(n).count('1')
  
#T:O(n), where n is number of bits
#S:O(1)