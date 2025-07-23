Binary Search
What it is: An algorithm used to find an element within a sorted array.
How it works: It repeatedly divides the search interval in half. It compares the target value to the middle element of the array.
If they match, the search is over.
If the target is less than the middle element, it narrows the search to the lower half.
If the target is greater, it narrows the search to the upper half.
Prerequisite: The data must be stored in a sorted, contiguous block of memory, like an array or list.
Use Case: Ideal for searching in a static, sorted dataset that doesn't change often. For example, looking up a word in a dictionary or finding a value in a sorted list of numbers.
Performance:
Search: Very fast, O(log n).
Insertion/Deletion: Not applicable directly. To keep the array sorted after an insertion or deletion, you would need to shift elements, which takes O(n) time.
Analogy: Imagine finding a name in a physical phone book. You don't start at 'A' and read every name. You open it to the middle, see if your name is before or after that page, and then repeat the process on that smaller section. That's binary search.