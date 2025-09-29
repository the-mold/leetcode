class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr1 = self.process_backspaces(s)
        arr2 = self.process_backspaces(t)

        print(arr1)
        print(arr2)

        return arr1 == arr2
    
    def process_backspaces(self, s):
        arr1 = []
        for i in range(len(s)):
            if len(arr1) == 0 and s[i] == "#":
                continue
                
            if len(arr1) > 0 and s[i] == "#":
                arr1.pop()
            else:
                arr1.append(s[i])
        
        return arr1
      
# T:O(m+n)
# S:O(m+n)
