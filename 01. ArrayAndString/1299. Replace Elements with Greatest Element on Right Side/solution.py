class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = [0 for _ in range(len(arr))] 

        last_idx = len(arr) - 1
        right[last_idx] = -1
        max_on_right = 0
        for i in range(last_idx - 1, -1, -1):
            max_on_right = max(max_on_right, arr[i+1])
            right[i] = max_on_right
        
        return right
