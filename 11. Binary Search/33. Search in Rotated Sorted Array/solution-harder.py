class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
    
            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Check if target is in the left sorted half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target is in the right sorted half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
    
#T: O(log n)
#S: O(1)
