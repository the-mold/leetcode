# What is the best data structure to store keys?
## Dictionary (Hash Table)
```
my_dict = {"key1": "value1", "key2": "value2"}
```
Time Complexity: O(1) average for lookups, insertions, and deletions
Best for: General-purpose key-value lookups when order doesn't matter
Advantages: Built-in, extremely fast for most use cases
## Set
```
my_set = {"key1", "key2", "key3"}
```
Time Complexity: O(1) average for lookups, insertions, and deletions
Best for: When you only need to store keys (no values) and check for membership
Advantages: Eliminates duplicates automatically, optimized for containment checks
collections.OrderedDict