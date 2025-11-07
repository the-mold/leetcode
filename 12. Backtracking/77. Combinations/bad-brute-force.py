from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Handle the edge case where k is 0, which results in one empty combination.
        if k == 0:
            return [[]]
        
        ans = []
        
        # 1. Initialize the first combination, which is simply [1, 2, ..., k].
        current_combo = list(range(1, k + 1))
        
        while True:
            # 2. Add a copy of the current combination to the answer list.
            ans.append(list(current_combo))
            
            # 3. Find the rightmost element that can be incremented.
            # We scan from right to left (from index k-1 down to 0).
            # The element at index 'i' can be incremented if it's not at its
            # maximum possible value, which is n - (k - 1 - i).
            index_to_increment = -1
            for i in range(k - 1, -1, -1):
                # Maximum value for current_combo[i] is n - (number of elements to its right)
                max_val_for_index = n - (k - 1 - i)
                if current_combo[i] < max_val_for_index:
                    index_to_increment = i
                    break
            
            # 4. If no element can be incremented, we have generated all combinations.
            # This happens when we reach the last combination, e.g., [n-k+1, ..., n].
            if index_to_increment == -1:
                break # Exit the while loop
            
            # 5. Generate the next combination.
            # Increment the found element.
            current_combo[index_to_increment] += 1
            
            # Update all subsequent elements to be consecutive numbers
            # following the incremented one.
            for i in range(index_to_increment + 1, k):
                current_combo[i] = current_combo[i - 1] + 1
                
        return ans
      
# Time Complexity: O(C(n, k) * k)
# The while loop runs exactly C(n, k) times (once for each combination).
# Inside the loop, the for loop to find the increment index runs k times in the worst case. The copy operation ans.append(list(current_combo)) also takes O(k).
# This gives a total time complexity of O(C(n, k) * k).

# Space Complexity: O(k)
# The current_combo list stores k elements. This is the only auxiliary space used besides the final answer list.