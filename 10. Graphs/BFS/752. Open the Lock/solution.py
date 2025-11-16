class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = collections.deque()
        q.append(("0000", 0)) #lock_combination, number_or_turns_to_get_here
        visited = set(deadends)

        def get_children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])

            return res

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns

            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))
        
        return -1

# Time: O(N + 10,000) = O(N + 10⁴)
# N for creating a set from deadends. 
# 10**4 or 10000 for states:
# -Each wheel has 10 digits (0-9)
# -4 wheels total
# -Total possible states: 10 × 10 × 10 × 10 = 10,000

# In practice:
# If N is small (≤ 500 as per constraints): O(10⁴) dominates
# The algorithm is effectively O(1) since 10⁴ is a constant upper bound

#Note! O(10000) is the same as O(1)

# Space Complexity
# Space: O(N + 10⁴)
# visited set: stores deadends + explored states (max 10,000 states)
# queue: max 10,000 states
# Total: O(10⁴) in worst case
#Note! O(10000) is the same as O(1)