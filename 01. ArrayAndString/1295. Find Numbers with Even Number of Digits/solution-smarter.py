class Solution:
    def is_even(self, num):
      digits = 0
      while num:
        digits += 1
        num //= 10

      # check if last bit of digits is 0, then the number is even
      return digits & 1 == 0
  
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_numbers = 0
        
        for num in nums:
          if self.is_even(num):
            even_digit_numbers += 1
        
        return even_digit_numbers
  