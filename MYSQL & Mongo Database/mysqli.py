# Install MySQL Driver
#python -m pip install mysql-connector-python
import mysql.connector

# Database Connection

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="core_python"
# )

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)

# 2 . To create a database in MySQL, use the "CREATE DATABASE" statement:

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")


# Check if Database Exists
# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

# print(mydb)

mycursor = mydb.cursor()



# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


# Primary Key
# When creating a table, you should also create a column with a unique key for each record.

# This can be done by defining a PRIMARY KEY.

# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#If the table already exists, use the ALTER TABLE keyword:

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)


# # sql = "INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')"
# # # val = ("John", "Highway 21")
# # mycursor.execute(sql)


# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


# # Insert Multiple Rows
# # To insert multiple rows into a table, use the executemany() method.

# # The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# #last Id Get
# print("1 record inserted, ID:", mycursor.lastrowid)


# Select From a Table
# To select from a table in MySQL, use the "SELECT" statement:

# mycursor.execute("SELECT * FROM customers")

# mycursor.execute("SELECT name, address FROM customers")

# # myresult = mycursor.fetchall()

# myresult = mycursor.fetchone()


# for x in myresult:
#   print(x)

#WHERE

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# MySQL Order By

# Sort the Result
# Use the ORDER BY statement to sort the result in ascending or descending order.

# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.


# sql = "SELECT * FROM customers ORDER BY name"

# # sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# Python MySQL Delete From By


# Delete Record
# You can delete records from an existing table by using the "DELETE FROM" statement:


# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# Python MySQL Drop Table

# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)

# Update Table
# You can update existing records in a table by using the "UPDATE" statement:


# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# MySQL Limit


# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# Start From Another Position
# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")


# Python MySQL Join


# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"


# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"