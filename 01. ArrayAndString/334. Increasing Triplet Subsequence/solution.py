import math

def increasingTriplet(nums: list[int]) -> bool:
    first_number = math.inf
    second_number = math.inf

    for num in nums:
        if num <= first_number:
            first_number = num
        elif num <= second_number:
            second_number = num
        else:
            return True
    
    return False
    
# T: O(n)
# S: O(1)

increasingTriplet([1, 5, 2, 6]) # True
increasingTriplet([1,1,1,1,1,1]) # False. To get False here, you must use <= operators above. Soltuion does not work with < operators.