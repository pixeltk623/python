from database import conn

mycursor = conn.cursor()

#mycursor.execute("CREATE DATABASE core_python")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)