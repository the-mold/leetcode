# to run tests: 
# ```
# python3 -m unittest ./test_lottery.py
# ```

import unittest
from solution import LotterySystem

class TestLotterySystem(unittest.TestCase):
  def setUp(self):
    self.lottery = LotterySystem()

  def test_init(self):
    self.assertEqual(self.lottery.tickets, [])
    self.assertEqual(self.lottery.total_amount, 0)

  def test_stats_empty(self):
    self.assertEqual(self.lottery.stats(), {
      "total_tickets": 0,
      "total_amount": 0,
      "avg_amount": 0,
    })
  
  def test_stats(self):
    self.lottery.buy_ticket("Alice", 20)
    self.lottery.buy_ticket("Bob", 10)

    self.assertEqual(self.lottery.stats(), {
      "total_tickets": 2,
      "total_amount": 30,
      "avg_amount": 15,
    })
