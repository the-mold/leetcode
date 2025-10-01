import unittest
from solution import SlidingWindowRateLimiter

class TestSlidingWindowRateLimiter(unittest.TestCase):
  def test_within_capacity_limit(self):
    rt = SlidingWindowRateLimiter(10, 90)
    self.assertTrue(rt.allow("user-1"))
    self.assertTrue(rt.allow("user-1"))
    self.assertTrue(rt.allow("user-1"))
    
  def test_capacity_exceeded(self):
    rt = SlidingWindowRateLimiter(2, 90)
    self.assertTrue(rt.allow("user-1"))
    self.assertTrue(rt.allow("user-1"))
    self.assertFalse(rt.allow("user-1"))
    
  def test_support_multiple_keys(self):
    rt = SlidingWindowRateLimiter(1, 90)
    self.assertTrue(rt.allow("user-1"))
    self.assertFalse(rt.allow("user-1"))
    
    self.assertTrue(rt.allow("user-2"))
    self.assertFalse(rt.allow("user-2"))
