import unittest
from TTLCache import TTLCache

class TestTTLCache(unittest.TestCase):
  def test_empy_cache(self):
    cache = TTLCache(100, 10)
    self.assertEqual(cache.get("user1"), -1)

  def test_item_stored_successfully(self):
    cache = TTLCache(100, 10)
    value = "value"
    cache.put("user1", value)
    self.assertEqual(cache.get("user1"), value)
