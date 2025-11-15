from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, returns all possible
        letter combinations that the number could represent.
        """
        # If the input is empty, as per the requirements, return an empty list.
        if not digits:
            return []

        # A mapping of digits to their corresponding letters.
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index: int, current_combination: str):
            """
            The recursive backtracking function.
            :param index: The current index in the `digits` string we are processing.
            :param current_combination: The string we have built so far.
            """
            # Base Case: If we have processed all digits, we have a complete solution.
            if index == len(digits):
                result.append(current_combination)
                return

            # Get the letters corresponding to the current digit.
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            # Explore the possibilities for the current digit.
            for letter in possible_letters:
                # Make a recursive call to explore the next digit,
                # adding the current letter to the combination.
                backtrack(index + 1, current_combination + letter)

        # Kick off the backtracking process starting from the first digit (index 0).
        backtrack(0, "")
        return result


# Time Complexity: O(N * M^N)
# The algorithm builds a recursion tree. The depth of this tree is N. At each level of the tree, we branch out for each possible letter of the current digit. In the worst case, we create M branches.
# This results in a total of M^N possible combinations (the leaf nodes of the tree).
# For each of these M^N combinations, we perform an operation to create the final string. In Python, creating the final string current_combination of length N takes O(N) time.
# Therefore, the total time complexity is the number of solutions multiplied by the time it takes to build each solution, which is O(N * M^N).

# Space Complexity: O(N) (excluding output) or O(N * M^N) (including output)
# The space complexity can be viewed in two ways:
# Excluding the output array: The main space usage comes from the recursion call stack. The maximum depth of the recursion is N (the length of the input digits). Therefore, the space complexity for the call stack is O(N).
# Including the output array: The result list stores all the generated combinations. As we established, there are M^N combinations, and each combination has a length of N. So, the space required to store the final result is O(N * M^N).
