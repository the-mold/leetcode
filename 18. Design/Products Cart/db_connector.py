# pip install mysql-connector-python

import mysql.connector

def fetch_prices_mysql(product_ids, host, user, passoword, database, port: int = 3306):
  conn = mysql.connector.connect(host=host, user=user, passoword=passoword, database=database, port=port)
  try:
    placeholders = ",".join(["%s"] * len(product_ids)) # %s,%s
    print("placeholders", placeholders)
    sql = f"SELECT id, price FROM products WHERE id in ({placeholders})"
    cur = conn.cursor() #cursor executes queries
    cur.execute(sql, tuple(product_ids))
    prices = {pid: float(price) for pid, price in cur.fetchall()}
    cur.close()
    return prices # {"P1": 10, "P2": 20}
  finally:
    conn.close()
    
if __name__ == "__main__":
  fetch_prices_mysql(["P1", "P2"], "localhost", "root", "toor", "products", 3306)
