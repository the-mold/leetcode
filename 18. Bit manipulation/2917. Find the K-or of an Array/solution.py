from typing import List

def find_k_or(nums: List[int], k: int) -> int:
    
    final_answer = 0

    # We will check each bit position, one by one.
    # Let's check positions 0 through 31.
    for position in range(32):
        
        # Let's count how many numbers have a '1' at this specific position.
        count_of_ones_at_this_position = 0
        
        for number in nums:
            # This is the magic trick to check if 'number' has a '1' at 'position'.
            # It will be 'True' if the bit is 1, and 'False' otherwise.
            is_the_bit_one = (number >> position) & 1
            
            if is_the_bit_one:
                count_of_ones_at_this_position += 1
        
        # Now, we check if our count is high enough.
        if count_of_ones_at_this_position >= k:
            
            # If it is, we need to add a '1' to our final answer at this 'position'.
            # This line does exactly that.
            value_to_add = (1 << position)
            final_answer += value_to_add
            
    return final_answer
  
# Time Complexity: O(N)
# The time complexity is O(N), which means the runtime grows linearly with the number of elements in the nums list.

# Here's why:

# Outer Loop: for position in range(32): This loop runs a fixed number of times (32). Since this number doesn't change no matter how large nums is, we consider it a constant factor.
# Inner Loop: for number in nums: This loop runs N times (once for each number in the input list).
# The total number of core operations is roughly 32 (from the outer loop) multiplied by N (from the inner loop). In Big O notation, we drop constant factors, so O(32 * N) simplifies to O(N).*

# Space Complexity: O(1)


  
# Intuition:
# Check Bit 0 (the 1's place):
# Which numbers have a 1 in this position?
# 7 (...1)
# 9 (...1)
# 9 (...1)
# 15 (...1)
# Count: 4 numbers.
# Decision: Is count >= k? Is 4 >= 4? Yes.
# So, the result will have a 1 in Bit 0.
# Result so far: ...0001
# Check Bit 1 (the 2's place):
# Which numbers have a 1 in this position?
# 7 (..1.)
# 15 (..1.)
# Count: 2 numbers.
# Decision: Is count >= k? Is 2 >= 4? No.
# So, the result will have a 0 in Bit 1.
# Result so far: ...0001 (unchanged)
# Check Bit 2 (the 4's place):
# Which numbers have a 1 in this position?
# 7 (.1..)
# 12 (.1..)
# 15 (.1..)
# Count: 3 numbers.
# Decision: Is count >= k? Is 3 >= 4? No.
# So, the result will have a 0 in Bit 2.
# Result so far: ...0001 (unchanged)
# Check Bit 3 (the 8's place):
# Which numbers have a 1 in this position?
# 12 (1...)
# 9 (1...)
# 8 (1...)
# 9 (1...)
# 15 (1...)
# Count: 5 numbers.
# Decision: Is count >= k? Is 5 >= 4? Yes.
# So, the result will have a 1 in Bit 3.
# Result so far: ...1001