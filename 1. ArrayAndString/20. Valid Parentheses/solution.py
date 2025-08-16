closing_to_openning_brackets_map = {
    ")": "(",
    "]": "[",
    "}": "{"
}
openning_brackets = {"(", "[", "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for idx, char in enumerate(s):
            if len(stack) == 0:
                stack.append(char)
            elif char in openning_brackets:
                # openning, just add
                stack.append(char)
            else:
                # closing, check if the previous item in stack is opening bracket
                if stack[-1] == closing_to_openning_brackets_map[char]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False

# Intuition
# For every closing bracket, check if previous was the correct openning bracket. If yes, pop the previous from the stack. Otherwise return False.


# Time Complexity: O(n)
# The time complexity is O(n) because the algorithm makes a single pass through the input string.

# Reasoning:

# The code uses a for loop that iterates through each character of the string s exactly once.
# Inside the loop, all operations performed for each character are constant time, or O(1):
# stack.append(): Adding an item to the end of a list (stack).
# stack.pop(): Removing an item from the end of a list.
# stack[-1]: Accessing the last item.
# Checking for membership in a set or dictionary (assuming openning_brackets and closing_to_openning_brackets_map are implemented efficiently).
# Since the loop runs n times and performs a constant amount of work in each iteration, the total time taken is directly proportional to the length of the string.

# Space Complexity: O(n)
# The space complexity is O(n) because, in the worst-case scenario, the stack could hold all the characters from the input string.

# Reasoning:

# The primary data structure that uses memory is the stack.
# Consider the worst-case input: a string consisting only of opening brackets, such as s = "(((((((" or s = "{[(".
# In this scenario, every character from the input string s will be pushed onto the stack, and none will be popped off until the end.
# Therefore, the maximum size of the stack will be equal to n, the length of the input string.