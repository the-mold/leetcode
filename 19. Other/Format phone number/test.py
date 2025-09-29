import unittest
from solution import format_numer

class TestFormatPhoneNumber(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(format_numer(""), "")
    
  def test_ending_three_two(self):
    self.assertEqual(format_numer("00-44 48 5555 8361"), "004-448-555-583-61")
  
  def test_ending_two_two(self):
    self.assertEqual(format_numer("0 - 22 1985--324"), "022-198-53-24")
