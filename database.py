import mysql.connector

conn = mysql.connector.connect(
		host="localhost",
		user="root",
		password=""
	)

if not conn:
	print("Db Error")