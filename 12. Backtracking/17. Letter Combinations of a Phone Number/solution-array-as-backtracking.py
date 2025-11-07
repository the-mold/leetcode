class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_number_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        n = len(digits)

        def backtracking(start, curr_combination):
            if len(curr_combination) == n:
                res.append("".join(curr_combination))
                return

            digit = digits[start]
            if digit not in phone_number_letter_map:
                return
            letters = phone_number_letter_map[digit]

            for letter in letters:
                curr_combination.append(letter)
                backtracking(start + 1, curr_combination)
                curr_combination.pop()

        backtracking(0, [])

        return res

# Let N be the length of the input digits string and K be the maximum number of letters a digit can map to (which is 4 for digits '7' and '9').
# Time Complexity: O(K^N * N)
# - K^N Combinations: In the worst case, every digit maps to K letters. The recursion tree will have a depth of N, and each level will branch up to K times. This results in roughly K^N leaf nodes, which correspond to the total number of combinations.
# - * N Work per Combination: For each of the K^N valid combinations, we perform a "".join(current_path) operation. Since the path has length N, this join operation takes O(N) time.
# - Total: The total time is the number of combinations multiplied by the work done for each, giving O(K^N * N).

# Space Complexity: O(N)
# - This complexity refers to the auxiliary space used by the algorithm, excluding the space required for the output result list.
# - Recursion Depth: The maximum depth of the recursion call stack will be N, as the backtrack function is called once for each digit in the input string.
# - current_path: The current_path list stores the combination being built, and its maximum length is N.
# - Total: The space required is dominated by the recursion stack and the path, both of which are proportional to N. Therefore, the space complexity is O(N).
