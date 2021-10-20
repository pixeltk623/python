# import json

# x =  '{"name":"John", "age":30, "city":"New York"}'

# z = json.loads(x)

# print(z)

# import re

# pattern = '[abc]'
# test_string = 'abc de ca'
# result = re.match(pattern, test_string)

# if result:
# 	print("Matched")
# else:
# 	print("Not Matched")



# import re

# string = 'atkj hi. Howdy'
# pattern = '[abc]'

# result = re.findall(pattern, string) 
# print(result)


import re

# string = 'Twelve:12 Eighty nine:89.'
# pattern = '\d+'

# result = re.split(pattern, string,2) 
# print(result)


# string = 'abc 12\
# de 23 \n f45 6'

# # matches all whitespace characters
# pattern = '\s+'

# # empty string
# replace = ''

# new_string = re.sub(pattern, replace, string) 
# print(new_string)


# string = 'sharvan Kumar'

# # matches all whitespace characters
# pattern = '[tezt]'
# replace = ''

# match = re.search(pattern, string)

# if match:
# 	print("Matched")
# else:
# 	print("Not")



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# if not mydb:
# 	print("Db Error")


mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE test_python")


