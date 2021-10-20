# Python program to create a table

from tkinter import *
import mysql.connector
# take the data

conn = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "",
			database = "getri"
		)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM tkinter")

myresult = mycursor.fetchall()


lst = myresult

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
root = Tk()
for i in range(total_rows):
	for j in range(total_columns):
		e = Entry(root, width=20, fg='blue',
					font=('Arial',16,'bold'))
		e.grid(row=i, column=j)
		e.insert(END, lst[i][j])
root.mainloop()
