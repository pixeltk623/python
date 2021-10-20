import mysql.connector

# connect() => Db Connect 
# cursor()
# execute()
# executemany()
# commit()
# fetchall()
# fetchone()


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE django")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# name = input("Enter Your Name")
# email = input("Enter Your Email")
# mobile = input("Enter Your Mobile") 


# print(type(name))	

# exit()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="django"
)

# print(mydb)

mycursor = mydb.cursor()



# query = "INSERT INTO `users`(`name`, `email`, `mobile`) VALUES ('"+name+"','"+email+"','"+mobile+"')"

# print(query)

# mycursor.execute(query)


# mydb.commit()


# print(mycursor.rowcount, "record inserted.")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


# sql = "INSERT INTO users (name, email,mobile) VALUES (%s, %s, %s)"
# val = ("John", "s@gmail.com", "8160410477")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO users (name, email,mobile) VALUES (%s, %s, %s)"

# val = ("John", "s@gmail.com", "8160410477")

# mycursor.execute(sql, val)


vals = [
  ["John", "s@gmail.com", "8160410477"],
  ["John", "s@gmail.com", "8160410477"],
  ["John", "s@gmail.com", "8160410477"],
  ["John", "s@gmail.com", "8160410477"],
  ["John", "s@gmail.com", "8160410477"]
]

mycursor.executemany(sql, vals)

mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# print(mycursor.lastrowid)


# num = 0
# insert_ids = []

# for arg in vals:
#     mycursor.execute(sql, arg)
#     insert_ids.append(mycursor.lastrowid)
#     mydb.commit()


# print(insert_ids[-1])


mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()


for x in myresult:
  print(x)


# print(myresult)