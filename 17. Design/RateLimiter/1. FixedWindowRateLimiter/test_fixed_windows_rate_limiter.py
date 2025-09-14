import unittest
from solution import FixedWindowRateLimiter

class TestFixedWindowsRateLimiter(unittest.TestCase):
  def test_allow_within_capacity(self):
    rl = FixedWindowRateLimiter(3, 90)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), True)
  
  def test_do_not_allow_over_capacity(self):
    rl = FixedWindowRateLimiter(3, 90)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), False)

  def test_keys_are_independent(self):
    rl = FixedWindowRateLimiter(1, 90)
    self.assertEqual(rl.allow("user-1"), True)
    self.assertEqual(rl.allow("user-1"), False)
    
    self.assertEqual(rl.allow("user-2"), True)
    self.assertEqual(rl.allow("user-2"), False)
