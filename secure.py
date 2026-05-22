import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# ============================================================
# TASK 4: Parameterised (safe) queries using ? placeholders
# ============================================================

def search_product_safe(name):
    # Validate input (Task 5)
    if not isinstance(name, str):
        print("Error: name must be a string")
        return None
    if len(name) < 2:
        print(f"Error: search term '{name}' is too short (minimum 2 characters)")
        return None
    if any(ch in name for ch in ['<', '>', ';']):
        print(f"Error: search term contains forbidden characters (< > ;)")
        return None

    # Safe parameterised query - user input goes in as data, never as SQL
    query = 'SELECT * FROM products WHERE name LIKE ?'
    rows = conn.execute(query, (f'%{name}%',)).fetchall()
    print(f'Result: {rows}')
    return rows

def login_safe(username, password):
    # Validate input (Task 5)
    if not isinstance(username, str) or not username:
        print("Error: username must be a non-empty string")
        return None
    if ' ' in username:
        print(f"Error: username '{username}' must not contain spaces")
        return None
    if not isinstance(password, str) or len(password) < 6:
        print(f"Error: password must be at least 6 characters long")
        return None

    # Safe parameterised query - ? placeholders prevent injection
    query = 'SELECT * FROM users WHERE username=? AND password=?'
    row = conn.execute(query, (username, password)).fetchone()
    print(f'Result: {row}')
    return row


# ============================================================
# TASK 4 TESTS - all 4 attacks must return [] or None
# ============================================================
print("=== Task 4: Attack payloads against secure functions ===\n")
print("Test 1 (OR 1=1 dump):")
print('Test 1:', search_product_safe("' OR 1=1--"))

print("\nTest 2 (UNION steal users):")
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))

print("\nTest 3 (admin login bypass):")
print('Test 3:', login_safe("admin'--", 'anything'))

print("\nTest 4 (always-true login):")
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))


# ============================================================
# TASK 5 TESTS - validation accepts/rejects correctly
# ============================================================
print("\n=== Task 5: Input Validation Tests ===\n")

print("search_product_safe('cement') - should WORK:")
search_product_safe('cement')

print("\nsearch_product_safe('') - should be REJECTED:")
search_product_safe('')

print("\nsearch_product_safe('<script>') - should be REJECTED:")
search_product_safe('<script>')

print("\nlogin_safe('admin', 'admin123') - should WORK:")
login_safe('admin', 'admin123')

print("\nlogin_safe('admin', 'ab') - should be REJECTED (password too short):")
login_safe('admin', 'ab')

print("\nlogin_safe('ad min', 'pass123') - should be REJECTED (space in username):")
login_safe('ad min', 'pass123')

conn.close()
