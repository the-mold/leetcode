def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    
    idx = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[idx - 2]:
            nums[idx] = nums[i]
            idx += 1
    
    return idx

removeDuplicates([1,1,1,2,2,3])