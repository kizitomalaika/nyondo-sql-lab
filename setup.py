import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Create products table
conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

# Create users table (needed for Task 3)
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'attendant'
)
''')

# Insert 5 products
conn.executemany(
    'INSERT INTO products (name, description, price) VALUES (?, ?, ?)',
    [
        ('Cement (bag)', 'Portland cement 50kg bag', 35000),
        ('Iron Sheet 3m', 'Gauge 30 roofing sheet 3m long', 110000),
        ('Paint 5L', 'Exterior wall paint white 5L', 60000),
        ('Nails 1kg', 'Common wire nails 1kg pack', 12000),
        ('Timber 2x4', 'Pine timber plank 2x4 per metre', 25000),
    ]
)

# Insert users
conn.execute('''
INSERT OR IGNORE INTO users (username, password, role) VALUES
    ('admin', 'admin123', 'admin'),
    ('fatuma', 'pass456', 'attendant'),
    ('wasswa', 'pass789', 'manager')
''')

conn.commit()

print("=== Products Table ===")
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)

print("\n=== Users Table ===")
users = conn.execute('SELECT * FROM users').fetchall()
for u in users:
    print(u)

conn.close()
