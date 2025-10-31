class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            l, r = 0, len(nums) - 1

            first_index = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] >= target:
                    # If mid is the target, it's a potential first position.
                    # Keep searching on the left side to find an even earlier one.
                    if nums[mid] == target:
                        first_index = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return first_index

        def find_last(nums, target):
            l, r = 0, len(nums) - 1

            last_index = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= target:
                    # If mid is the target, it's a potential last position.
                    # Keep searching on the right side to find an even later one.
                    if nums[mid] == target:
                        last_index = mid
                    l = mid + 1
                else:
                    r = mid - 1

            return last_index
        
        first = find_first(nums, target)
        last = find_last(nums, target)

        return [first, last]
    
# T: O(log n)
# S: O(1)