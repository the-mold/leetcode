class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        peak = (-1,-1)
        for idx, val in enumerate(arr):
            if peak[1] < val:
                peak = (idx, val)

        # check left
        if peak[0] == 0:
            return False
        for i in range(peak[0], -1, -1):
            if i == 0:
                break
            if arr[i-1] >= arr[i]:
                return False

        # check right
        if peak[0] == n-1:
            return False
        for i in range(peak[0], n - 1):
            if arr[i] <= arr[i+1]:
                return False

        return True

# T:O(n)
#S:O(1)
