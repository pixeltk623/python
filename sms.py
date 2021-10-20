import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="php_11_aug"
)

mycursor = mydb.cursor()

query = "SELECT name,mobile FROM users"
mycursor.execute(query)
myresult = mycursor.fetchall()

#data_keys = myresult.keys()

# variable = {for key,val in myresult}


# print(variable)
student = []
for x in range(len(myresult)):
	student.append({"name": myresult[x][0], "mobile": myresult[x][1].replace(" ", "")})


from twilio.rest import Client

account_sid = "ACcf617ef07f0b303abb37a1746cce8615"
auth_token = "a41e4449187ca561de5f3ce802fa9cac"
client = Client(account_sid, auth_token)

# for number in student:
# 	print(number['name'])
# sentence.replace(" ", "")

print(student)
exit()

for number in student:
	message = client.messages.create(
	                              body='Hi there'+number['name'],
	                              from_='+18788776105',
	                              to=number['mobile']
	                          )

print(message.sid)