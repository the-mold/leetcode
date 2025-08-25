class Solution:
    def binarySearch(seld, nums, target, left, right):
        l = left
        r = right

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Finding smallest element in array!!!
        # You can use binary search for it! It works for rotated and not rotated arrays!
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

        # Note: at this pointing to the smallest element

        # now try to find target in the left half of the array:
        ans = self.binarySearch(nums, target, 0, l - 1)
        if ans != -1:
            return ans

        # now try the right half
        return self.binarySearch(nums, target, l, len(nums) - 1)
    
    [0,1,2,3,4]