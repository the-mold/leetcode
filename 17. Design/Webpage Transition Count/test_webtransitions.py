# to run tests: 
# ```
# python3 -m unittest ./test_lottery.py
# ```

import unittest
from solution import find_most_frequest_transition

class TestWebtransitions(unittest.TestCase):
  def setUp(self):
    self.test_data = [
      "user1 /",
      "user1 /account",
      "user2 /service",
      "user2 /service/sub",
      "user3 /",
      "user3 /account",
    ]

  def test_no_logs(self):
    self.assertEqual(find_most_frequest_transition([]), {
      "max_transitions": 0,
      "most_frequet_transition": None,
    })

  def test_logs(self):
    self.assertEqual(find_most_frequest_transition(self.test_data), {
      "max_transitions": 2,
      "most_frequet_transition": ("/", "/account"),
    })
