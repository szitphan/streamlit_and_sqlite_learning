import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')


# Create a cursor
c = conn.cursor()


# # Create a table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
# )""")


# Inset a record into table
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")


# # Insert many records into table
# many_customers = [
#     ('Wes', 'Brown', 'wes@brown.com'),
#     ('Steph', 'Kuewa', 'steph@kuewa'),
#     ('Dan', 'Pas', 'dan@pas.com'),
# ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)




# Query the database
# c.execute("SELECT * FROM customers")
# c.execute("SELECT rowid, * FROM customers")
c.execute("""
          SELECT * 
          FROM customers
          WHERE last_name = 'Pas'
          """)
c.execute("""
          SELECT * 
          FROM customers
          WHERE email LIKE '%codemy.com'
          """)

# c.fetchone()
# c.fetchmany(3)
items = c.fetchall()

for item in items:
    print(item)


# Update records


# Commit our command
conn.commit()


# Close our command
conn.close
