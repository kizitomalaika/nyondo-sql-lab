import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

print("=== Query A: Every column of every product ===")
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)

print("\n=== Query B: Name and price of all products ===")
rows = conn.execute('SELECT name, price FROM products').fetchall()
for r in rows:
    print(r)

print("\n=== Query C: Full details of product with id = 3 ===")
rows = conn.execute('SELECT * FROM products WHERE id = 3').fetchall()
for r in rows:
    print(r)

print("\n=== Query D: Products whose name contains 'sheet' (partial match) ===")
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for r in rows:
    print(r)

print("\n=== Query E: All products sorted by price, highest first ===")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for r in rows:
    print(r)

print("\n=== Query F: The 2 most expensive products ===")
rows = conn.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for r in rows:
    print(r)

print("\n=== Query G: Update Cement (id=1) price to 38,000 then confirm ===")
conn.execute('UPDATE products SET price = 38000 WHERE id = 1')
conn.commit()
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)

conn.close()
