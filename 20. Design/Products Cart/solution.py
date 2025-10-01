def calculate_total(order_products, prices, discounts, order_threshold, order_discount):
  total = 0
  for order in order_products:
    product_id = order.get("id")
    qty = order.get("quantity")
    
    if product_id not in prices:
      raise Exception(f"unknow product: {product_id}")
  
    price = prices[product_id]
    discount = 0
    if product_id in discounts:
      discount = discounts[product_id]
    
    product_price = price * qty * (1 - discount)
    total += product_price
  
  if order_threshold and total >= order_threshold:
    total = total * (1 - order_discount)
  
  return round(total, 2)


if __name__ == "__main__":
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
  
  calculate_total(products, prices, discounts, 100, 0.1)
  