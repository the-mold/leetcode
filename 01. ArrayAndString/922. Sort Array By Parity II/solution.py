class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd_idx = 1

        for even_idx in range(0, n, 2):
            if nums[even_idx] & 1 != 0:
                # needs swapping

                # search odd index number that is even(hence places wrongly) 
                # Do while loop, while numbers are odd. When loop stops, you found
                # an odd index that has even number in it.
                while nums[odd_idx] & 1 == 1:
                    odd_idx += 2
                
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
 
        return nums
      
# T:O(n)
# Even though there is a while loop inside the for loop, it's not O(n²). Here's why:
# even_idx Pointer: The for loop pointer (even_idx) iterates through the even positions of the array. It will check n/2 elements in total.
# odd_idx Pointer: The while loop pointer (odd_idx) only ever moves forward. It starts at 1 and increments by 2 each time it moves. It never resets.
# In the worst-case scenario, both pointers (even_idx and odd_idx) will collectively pass through the entire array just once. Each element is visited a constant number of times, making the overall time complexity linear, or O(n).

# S:O(1)
