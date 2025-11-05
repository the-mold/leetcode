class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(current_numbers, start_idx):
            if len(current_numbers) == k:
                ans.append(list(current_numbers))
                return

            for i in range(start_idx, n + 1):
                current_numbers.append(i)
                backtracking(current_numbers, i+1)
                current_numbers.pop()

        backtracking([], 1)

        return ans

# T: O(C(n,k) × k) or more detailed: O( n!/((k-1)!*(n-k)!) )
#Better learn O(C(n,k) × k) which is number of combinations of n and k multiplied bu size of each combination k.

# S:O(k)
