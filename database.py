import sqlite3

# # Connect to database
# conn = sqlite3.connect('customer.db')


# # Create a cursor
# c = conn.cursor()


# # # Create a table
# # c.execute("""CREATE TABLE customers (
# #         first_name text,
# #         last_name text,
# #         email text
# # )""")


# # Inset a record into table
# # c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")


# # # Insert many records into table
# # many_customers = [
# #     ('Wes', 'Brown', 'wes@brown.com'),
# #     ('Steph', 'Kuewa', 'steph@kuewa'),
# #     ('Dan', 'Pas', 'dan@pas.com'),
# # ]

# # c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)




# # Query the database
# # c.execute("SELECT * FROM customers")
# # c.execute("SELECT rowid, * FROM customers")
# c.execute("""
#           SELECT * 
#           FROM customers
#           WHERE last_name = 'Pas'
#           """)
# c.execute("""
#           SELECT * 
#           FROM customers
#           WHERE email LIKE '%codemy.com'
#           """)

# # Query the database - Order by
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# # Query the database - Limit results
# c.execute("SELECT rowid, * FROM customers LIMIT 2")


# # c.fetchone()
# # c.fetchmany(3)
# items = c.fetchall()

# for item in items:
#     print(item)


# # Update records
# c.execute("""
#           UPDATE customers SET first_name  = 'Marty'
#           WHERE last_name = 'Brown')  # this case can cause issues when having the same 1st name
#           """)
# c.execute("""
#           UPDATE customers SET first_name  = 'Marty'
#           WHERE rowid = '1')
#           """)

# # Delete records
# c.execute("""
#           DELETE from customer
#           WHERE rowid = 6
#           """)
          
# # Commit our command
# conn.commit()


# # Close our command
# conn.close

def add_record(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close

def get_data(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    return items
