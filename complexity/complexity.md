# Time Complexity
1. O(1) – Constant Time. 
Most efficient. Independent of input size.
Example: Dictionary lookup (dict[key]), Set lookup (x in set)

#GOOD Performance---------
2. O(log n) – Logarithmic Time. 
Problem size reduces by half each step.
Example: Binary Search.

What is log(n)?
There is en exponent 2**5 = 32
The `log` operation is reverse to it: log(32) = 5. It asks to which power do i need to raise 2 to get 32?

3. O(n) – Linear Time. 
Scales directly with input size.
Example: Looping through an array(for loop, sum(nums), max(nums)).
4. O(n log n) – Quasilinear Time
Slightly worse than O(n), common in sorting algorithms(it is in Python!)
Example: Merge Sort, QuickSort (average case).

#SLOW Performance---------
5. O(n²) – Quadratic Time
Nested loops make performance slow.
Example: Bubble Sort, Selection Sort, Insertion Sort.

Note: everyting that is n to the power of some constant is called polynomial time.

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
Rule of thumb: branching factor in DYNAMIC. It is not constant. See screenshots in examples and compare exponential to factorial.
In exponential you always branch in constant way. In factorial branching is dynamic(it is changing).
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
O(2ⁿ) or O(n!): Recursive problems with branching factors (e.g., Fibonacci, Backtracking).
See screenshots in `examples`.

Python examples:
#Array
if c in vowels:     #O(n)
#Set
if c in vowels:     #O(1)

#max, min, sum
O(n)

#sort
O(n log n)


## Common situations

### Positive arithmetic progression
```
for i in range(n):
    for j in range(i + 1):
        # some constant time operation
```
- Outer Loop: The for i in range(n): loop runs n times, for i from 0 to n-1.
- Inner Loop: The for j in range(i + 1, n): loop's number of iterations increases as i increases.
    - When i is 0, the j is 1
    - when i is 1, the j is 2
    ...
    - when i is n-1, the j is n
- Total Operations: To find the total number of times the inner block executes, we need to sum the number of inner loop iterations for each outer loop iteration. This gives us the sum of an arithmetic series: 1 + 2 + 3 + ... + n
- The Formula: The sum of the first n integers is given by the formula: n * (n + 1) / 2
- Big O Notation: If we expand the formula, we get (n² + n) / 2. In Big O notation, we are interested in the dominant term as n grows large, and we ignore constant factors.
    - The n² term grows much faster than the n term.
    - We drop the n term and the constant factor of 1/2.
This leaves us with O(n²).

### Negative arithmetic progression
```
for i in range(n):
    for j in range(i + 1, n):
        # some constant time operation
```
- Outer Loop: The for i in range(n): loop runs n times, for i from 0 to n-1.
- Inner Loop: The for j in range(i + 1, n): loop's number of iterations decreases as i increases.
    - When i is 0, the inner loop runs n-1 times (for j from 1 to n-1).
    - When i is 1, the inner loop runs n-2 times (for j from 2 to n-1).
    ...
    - When i is n-2, the inner loop runs 1 time (for j = n-1).
    - When i is n-1, the inner loop runs 0 times (the range (n, n) is empty).
- Total Operations: The total number of times the inner block is executed is the sum of these iterations: (n-1) + (n-2) + ... + 1 + 0
- The Formula: This is the sum of the first n-1 integers. Using the arithmetic series sum formula k * (k+1) / 2 where k = n-1, we get: (n-1) * ((n-1) + 1) / 2 = (n-1) * n / 2 = (n² - n) / 2
- Big O Notation: As with the last example, we focus on the term that grows the fastest as n gets large and we drop constant factors.
The dominant term is n².
We ignore the -n term and the 1/2 constant.



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
Python sorting SPACE complexity is O(n).
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
