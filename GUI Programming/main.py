# GUI => Graphical user interface
# Tkinter => GUI Library
# fast easy

# 1. Import the Tkinter
# 2. Create  the main window
# 3. Add any number of widgets to the main window
# 4. Apply the event trigger on the widgets

# tk() -> To create a main window tkinter provide a method
# mainloop() -> there is a method known by the name mainloop() , it is  used to run your application


# button() 
# Entry()
# Lable()


# import tkinter

from tkinter import *
import mysql.connector
import tkinter.messagebox as m

def connectionWithMysqli():
	mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="",
		  database="pymysql"
		)
	return mydb

def insertData():
	r = ern.get()
	f = efn.get()
	l = eln.get()
	e = email.get()

	if (r=='' or f == '' or l == '' or e == ''):
		m.showinfo("Insert Status", "All Fields are required")
	else:
		try:
			conn = connectionWithMysqli()
			cursor = conn.cursor()
			args = (r,f,l,e)
			query = "INSERT INTO `students`(`rollno`, `fname`, `lname`, `email`) VALUES (%s,%s,%s,%s)"
			cursor.execute(query,args)
			conn.commit()
			m.showinfo("InsertStatus", "Data Inserted")
			conn.close()

		except Exception as e:
			print("Insert Exception ", e)
		


r = Tk()
r.geometry("500x500")
r.title("My Title")
r.configure(bg="lightblue")

rn = Label(r, text="Roll No")
rn.place(x=20,y=20)

fn = Label(r, text="First Name")
fn.place(x=20,y=60)

ln = Label(r, text="Last Name")
ln.place(x=20,y=100)


em = Label(r, text="Email")
em.place(x=20,y=140)


ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=60)


eln = Entry()
eln.place(x=100,y=100)

email = Entry()
email.place(x=100,y=140)

button1 = Button(r, text="Insert", bg="White", command=insertData)
button1.place(x=20, y=180)
mainloop()

