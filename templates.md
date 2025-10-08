# Two pointer
```
  l = 0
  r = len(nums) - 1
  while l < r:
```

# Binary search
l = 0
r = len(nums) - 1
while l <= r:
  mid = (l + r) // 2



# Handling Edge cases--------------------
1. Input Size and Structure
-Empty Inputs: What if the input is an empty array, string, list, or hash map? ([], "", None).
-Single-Element Inputs: How does your algorithm behave with just one element? ([5], "a").
-All Elements are Identical: Inputs where all elements are the same ([3, 3, 3, 3]).
-Very Large Inputs: Consider the performance implications. Will your solution hit time or memory limits? Think about integer overflow for large numbers.
2. Special Values
Zeros: How does your code handle 0? Does it involve division or multiplication by zero?
Negative Numbers: Does the logic change for negative values?
None, null, or undefined: If the language supports it, can inputs be null?
Duplicates: How does your algorithm handle duplicate values in a collection? Is it supposed to preserve them or treat them uniquely?
3. Positional Edge Cases
First and Last Elements: Does your logic correctly handle operations on the very first or very last element of a sequence? (e.g., pointers going out of bounds).
Target Not Found: For search-related problems, what happens if the target value doesn't exist in the input?
Cycles: In problems involving graphs or linked lists, could there be a cycle? How would you detect and handle it?
Skewed Data Structures: For tree problems, what if the tree is heavily unbalanced or just a single long chain of nodes (like a linked list)?
How to Approach Edge Cases in an Interview
Clarify Assumptions: Before you start coding, ask the interviewer about the constraints. For example: "Are the numbers always positive?" or "Can the input list be empty?"
Brainstorm Before Coding: Take a minute to list out potential edge cases for the specific problem. This shows you're thinking ahead.
Handle Upfront: Often, you can check for simple edge cases (like an empty input) at the very beginning of your function. This can simplify the main logic.
Test Your Solution: After writing your code, mentally walk through it with your brainstormed edge cases to see if it holds up. For instance, trace your pointers with an empty array or a single-element array.