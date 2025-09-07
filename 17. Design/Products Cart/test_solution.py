import unittest
from solution import calculate_total

class TestOrderPrice(unittest.TestCase):
  def test_single_product(self):
    products = [
      {"id": "P1", "quantity": 1},
    ]
    prices = {
      "P1": 10,
      "P2": 20,
      "P3": 30
    }
    discounts = {
      "P3": 0.1
    }
    act = calculate_total(products, prices, discounts, 100, 0.1)
    self.assertEqual(act, 10)

  def test_product_discount(self):
    products = [
      {"id": "P1", "quantity": 1},
    ]
    prices = {
      "P1": 10,
      "P2": 20,
      "P3": 30
    }
    discounts = {
      "P1": 0.1
    }
    act = calculate_total(products, prices, discounts, 100, 0.1)
    self.assertEqual(act, 9)

  def test_theshold_discount(self):
    products = [
      {"id": "P1", "quantity": 1},
    ]
    prices = {
      "P1": 10,
      "P2": 20,
      "P3": 30
    }
    discounts = {
      "P3": 0.1
    }
    act = calculate_total(products, prices, discounts, 10, 0.1)
    self.assertEqual(act, 9)
  
  def test_product_combination(self):
    products = [
      {"id": "P1", "quantity": 1},
      {"id": "P2", "quantity": 2},
      {"id": "P3", "quantity": 3},
    ]
    prices = {
      "P1": 10,
      "P2": 20,
      "P3": 30
    }
    discounts = {
      "P3": 0.1
    }
    act = calculate_total(products, prices, discounts, 100, 0.1)
    self.assertEqual(act, 117.90)
