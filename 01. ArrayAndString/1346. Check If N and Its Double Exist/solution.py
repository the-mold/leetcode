class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sett = set()
        for num in arr:
            if num * 2 in sett or num / 2 in sett:
                return True

            sett.add(num)
        
        return False
      
#T:O(n)
#S:O(n)
