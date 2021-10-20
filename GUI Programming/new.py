from tkinter import *
import mysql.connector
import tkinter.messagebox as m



from datetime import timedelta


def connectDb():
	mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="",
		  database="tkinter"
		)
	return mydb

def insertData():
	rl = ern.get()
	f = efn.get()
	l = eln.get()
	e = ee.get()
	
	if (rl=='' or f == '' or l =='' or e == ''):
		m.showinfo("Insert Status", "All Fields are required")
	else:
		try:
			conn = connectDb()
			cursor = conn.cursor()
			args = (f,l,e)
			query = "INSERT INTO students (`fname`, `lname`, `email`) VALUES (%s, %s, %s)";
			cursor.execute(query,args)
			conn.commit()
			m.showinfo("InsertStatus", "Data Inserted")
			conn.close()
		except Exception as e:
			print("Insert Exception ", e)
		

r = Tk()
r.geometry("300x300")
r.title("List")
r.configure(bg="lightblue")
rn = Label(r, text="Roll No")
rn.place(x=50,y=20)

fn = Label(r, text="First Name")
fn.place(x=50,y=60)

ln = Label(r, text="Last Name")
ln.place(x=50,y=100)

email = Label(r, text="Email")
email.place(x=50,y=140)

ern = Entry()
ern.place(x=120,y=20)

efn = Entry()
efn.place(x=120,y=60)

eln = Entry()
eln.place(x=120,y=100)


ee = Entry()
ee.place(x=120,y=140)

button1 = Button(r, text="Submit", bg="White", command=insertData)
button1.place(x=120,y=180)

mainloop()