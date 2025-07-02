# Time Complexity
1. O(1) – Constant Time. 
Most efficient. Independent of input size.
Example: Dictionary lookup (dict[key]), Set lookup (x in set)

#GOOD Performance---------
2. O(log n) – Logarithmic Time. 
Problem size reduces by half each step.
Example: Binary Search.
3. O(n) – Linear Time. 
Scales directly with input size.
Example: Looping through an array(for loop, sum(nums), max(nums)).
4. O(n log n) – Quasilinear Time
Slightly worse than O(n), common in sorting algorithms.
Example: Merge Sort, QuickSort (average case).

#SLOW Performance---------
5. O(n²) – Quadratic Time
Nested loops make performance slow.
Example: Bubble Sort, Selection Sort, Insertion Sort.

#Worst Performance---------
6. O(2ⁿ) – Exponential Time
Each step doubles the work, making it extremely inefficient.
Example: Naïve Fibonacci recursion, Backtracking problems.
```
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(2ⁿ)
```

7. O(n!) – Factorial Time
The worst complexity, common in permutation problems.
Example: Generating all permutations (brute force).
```
def permute(nums, path=[]):
    if not nums:
        print(path)  # O(n!)
        return
    for i in range(len(nums)):
        permute(nums[:i] + nums[i+1:], path + [nums[i]])
```

# How to Estimate Complexity?
1. Check if sorting is involved: likely `O(n log n)`.
2. Count loops:
Single loop? `O(n)`
One loop after another? `O(n + m)` which is `O(n)`
Nested loops? `O(n^(number_of_loops))`

3. Check for recursion → Estimate calls and tree size.
O(log n): If a problem size is halved each step (e.g., Binary Search).
O(n log n): Merge Sort, QuickSort.
O(2ⁿ) or O(n!): Recursive problems (e.g., Fibonacci, Backtracking).



# Space(Memory) Complexity
#Best---------
1. O(1) – Constant Space (Best)
Memory usage does NOT grow with input size.
Only a few variables are used (no extra arrays, lists, or recursion stacks).
```
def swap(a, b):
    a, b = b, a  # O(1) space (only two variables)
    return a, b
```

#Efficient-------
2. O(log n) – Logarithmic Space
Occurs in recursive algorithms that reduce the problem size by half.
Example: Recursive Binary Search (O(log n) call stack)

#Moderate-------
3. O(n) – Linear Space
Memory grows proportionally to input size (n).
Example: Storing a new list or using recursion up to depth n.
Python sorting is O(n).
```
def duplicate_array(arr):
    return arr[:]  # Creates a new list, O(n) space
```

#Heavy memory usage-----
4. O(n log n) – Quasilinear Space
Occurs in sorting algorithms that use extra storage.
Example: Merge Sort (uses extra arrays in recursion).

#Worst memory usage-----
5. O(n²) – Quadratic Space
Occurs when storing a 2D table (like in Dynamic Programming).
Example: DP Table in Floyd-Warshall Algorithm or Matrix Multiplication.

6. O(2ⁿ) – Exponential Space
Occurs in recursive problems generating all subsets or permutations.
Example: Storing all subsets of a set (Power Set).

7. O(n!) – Factorial Space
Worst case, used in problems generating all permutations.
Example: Traveling Salesman Problem, Backtracking.
