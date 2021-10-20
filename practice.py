
Python Program to Find the Largest Among Three Numbers
Python Program to Calculate the Area of a Triangle
Python Program to Swap Two Variables
Python Program to Convert Celsius To Fahrenheit
Python Program to Convert Kilometers to Miles
Python Program to Check Prime Number
Python Program to Print all Prime Numbers in an Interval
Python Program to Find the Factorial of a Number
Python Program to Display the multiplication Table
Python Program to Print the Fibonacci sequence
Python Program to Check Armstrong Number
Python Program to Find Armstrong Number in an Interval
Python Program to Find the Sum of Natural Numbers


# input()


# exit()
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def __str__(self):
#         return f'Person({self.first_name},{self.last_name},{self.age})'


# person = Person('John', 'Doe', 25)
# print(person)

# exit()
# import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# mydb = myclient['mongodatabase']
# mycol = mydb["students"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# print(x)

# exit()

# def bubbleSort(arr):
# 	for x in range(0,len(arr)-1):
# 		for y in range(0,len(arr)-x-1):
# 			if arr[y]>arr[y+1]:
# 				arr[y], arr[y + 1] = arr[y + 1], arr[y]







# allNumber = [45,78,98,12,78,63,88]
# bubbleSort(allNumber)
# print(allNumber)

# exit()
# # # Tuples are used to store multiple items in a single variable.

# # # A tuple is a collection which is ordered and unchangeable.


# # name = ("kumar","sanjeev","sharvan")

# # print(name)

# # # Tuple Items
# # # Tuple items are ordered, unchangeable, and allow duplicate values.

# # # Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# # print(name[0])

# # # Ordered
# # # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# # # Unchangeable
# # # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# # # name[0] = "kkkk"

# # # print(name)


# # name =  ("kumar","sanjeev","sharvan","sharvan")

# # print(name)

# # print(len(name))

# # listOfUser = ("name",)

# # print(type(listOfUser))

# # tuple1 = (1,2,3,4,8,8,9)
# # tuple2 = (True,False)

# # tuple3 = ("asda","dsad",True,545,"asdas")

# # print(type(tuple1))
# # print(type(tuple2))

# # print(type(tuple3))

# # print(tuple3)


# # # The tuple() Constructor
# # # It is also possible to use the tuple() constructor to make a tuple.

# # tuple3 = tuple(("asda","dsad",True,545,"asdas"))

# # print(tuple3)


# # new_tuple = ("kumar","sanjeev","sharvan","sharvan")

# # print(new_tuple[:4])

# # print(new_tuple[2:])


# # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # print(thistuple[-4:-1])


# # if "apple" in thistuple:
# # 	print("yes")
# # else:
# # 	print("no")


# # # Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# # # But there are some workarounds.

# # # Change Tuple Values
# # # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# # # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


# # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")


# # new_list = list(thistuple)

# # new_list[0] = "hello"

# # print(new_list)

# # new_list.append("last")

# # new_tuple = tuple(new_list)

# # print(new_tuple)

# # print(type(new_list))



# # # t1 = ("1","2","4","5")
# # # # t2 = (5,5,8)

# # # # t1 += t2

# # # # print(t1)

# # # t3 = list(t1)

# # # t4 = t3.remove("4")

# # # print(t4)

# # thistuple = ("apple", "banana", "cherry")
# # y = list(thistuple)
# # y.remove("apple")
# # thistuple = tuple(y)


# # print(thistuple)


# # thistuple = (5,5,8)

# # y = list(thistuple)
# # y.remove(5)
# # thistuple = tuple(y)


# # print(thistuple)


# # # del thistuple

# # print(thistuple)



# # # techno = ("PHP","Java","Python","Ruby")

# # # (back,spring,jango,r) = techno


# # # print(back)

# # # print(spring)

# # # print(jango)
# # # print(r)

# # # Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# # # Using Asterisk*
# # # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:


# # techno = ("PHP","Java","Python","Ruby")

# # (back,*spring,jango) = techno


# # print(back)
# # print(spring)
# # print(jango)

# techno = ("PHP","Java","Python","Ruby")

# for x in techno:
# 	print(x)


# print("\n")

# for x in range(len(techno)):
# 	print(techno[x])

# i = 0
# while i<len(techno):
# 	print(techno[i])
# 	i = i+1


# techno = ("PHP","Java","Python","Ruby")

# new = (True,True)

# print(techno*5)


# print(techno.index("PHP"))
# print(techno.count("PHP"))
# import pprint



# listOfStudent = {
# 	"name": "sharvan",
# 	"email": "s@gmail.com",
# 	"mobile": 9835401515,
# 	"doj": "2020-10-20",
# 	"colors": ["red", "white", "blue"]

# }


# print( listOfStudent.keys() )


# listOfStudent['name'] = "sanjeev"

# print(listOfStudent)

# print(listOfStudent.values())


# print(listOfStudent.items())

# print(listOfStudent.get("name"))

# print(type(listOfStudent))

# print(listOfStudent)

# pprint.pprint(listOfStudent)

# print(listOfStudent['doj'])

# print(len(listOfStudent))


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


# Python Program to calculate the square root

# Note: change this value for a different result
# num = 82

# # To take the input from the user
# #num = float(input('Enter a number: '))

# num_sqrt = num ** 0.5
# print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))


# num = 1234

# rev = 0
# while num > 0:
# 	rem = num%10
# 	rev = rev * 10 + rem
# 	num = int(num/10)

# print(rev)

# for i in range(6):
# 	for j in range(i):
# 		print(j+1, end="")

# 	print("\n")


# for x in range(1,10):
# 	print(x)

# exit()
# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, 5+1):

#     for space in range(1, (5-i)+1):
#         print(end="  ")


#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1

#     k = 0
#     print()

# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1



# import time

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec -= 1

#     print("stop")

# countdown(5)


# Python program to illustrate the concept
# of threading
# importing the threading module


# import threading

# def print_cube(num):
#   """
#   function to print cube of given num
#   """
#   print("Cube: {}".format(num * num * num))

# def print_square(num):
#   """
#   function to print square of given num
#   """
#   print("Square: {}".format(num * num))

# if __name__ == "__main__":
#   # creating thread
#   t1 = threading.Thread(target=print_square, args=(10,))
#   t2 = threading.Thread(target=print_cube, args=(10,))

#   # starting thread 1
#   t1.start()
#   # starting thread 2
#   t2.start()

#   # wait until thread 1 is completely executed
#   t1.join()
#   # wait until thread 2 is completely executed
#   t2.join()

#   # both threads completely executed
#   print("Done!")



# Python program to illustrate the concept
# of threading
# import threading
# import os

# def task1():
#   print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#   print("ID of process running task 1: {}".format(os.getpid()))

# def task2():
#   print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#   print("ID of process running task 2: {}".format(os.getpid()))

# if __name__ == "__main__":

#   # print ID of current process
#   print("ID of process running main program: {}".format(os.getpid()))

#   # print name of main thread
#   print("Main thread name: {}".format(threading.current_thread().name))

#   # creating threads
#   t1 = threading.Thread(target=task1, name='t1')
#   t2 = threading.Thread(target=task2, name='t2')

#   # starting threads
#   t1.start()
#   t2.start()

#   # wait until all threads finish
#   t1.join()
#   t2.join()


# import threading

# class MyThrd1(threading.Thread):
#   def run(self):
#     for i in range(1,5):
#         print("Hi This is Kumar")

# class MyThrd2(threading.Thread):
#   def run(self):
#     for i in range(1,5):
#         print("Hi This is Sharvan")

# t1 = MyThrd1()

# t2 = MyThrd2()

# t1.start()
# t2.start()

# print("Main is doing some work")
# t1.join()
# print("main finish")


# # define a list
# my_list = [4, 7, 0, 3]

# # get an iterator using iter()
# my_iter = iter(my_list)


# print(next(my_iter))
# print(next(my_iter))

# print(my_iter.__next__())


# iterate through it using next()

# # Output: 4
# print(next(my_iter))

# # Output: 7
# print(next(my_iter))

# # next(obj) is same as obj.__next__()

# # Output: 0
# print(my_iter.__next__())

# # Output: 3
# print(my_iter.__next__())

# # This will raise error, no items left
# next(my_iter)


# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""

#     def __init__(self, max=0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration


# # create an object
# numbers = PowTwo(3)

# # create an iterable from the object
# i = iter(numbers)

# # Using next to get to the next iterator element
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")



# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")


# Python - Change Dictionary Items


# listOfStudent = {
#   "name": "sharvan",
#   "email": "s@gmail.com",
#   "mobile": 9835401515,
#   "doj": "2020-10-20",
#   "colors": ["red", "white", "blue"]

# }


# print(listOfStudent)

# listOfStudent['email'] = "sss@ds.com"

# print(listOfStudent)

# listOfStudent.update({"doj":"2021-05-16"})

# print(listOfStudent)

# listOfStudent["ghar"] = "nalanda"

# print(listOfStudent)

# listOfStudent.update({"color":"red"})

# print(listOfStudent)


# listOfStudent.pop("color")

# print(listOfStudent)


# listOfStudent.popitem()

# print(listOfStudent)


# del listOfStudent["name"]

# print(listOfStudent)

# listOfStudent.clear()

# print(listOfStudent)

# del listOfStudent

# print(listOfStudent)


# for i in listOfStudent.items():
#     print(i)

# newD = listOfStudent.copy()

# newR = dict(listOfStudent)

# print(newR)


# print(newD)


# myFamily = {
#         "child1" : {
#             "name" : "Emil",
#             "year" : 2004
#         },
#         "child2" : {
#             "name" : "Emil",
#             "year" : 2004
#         },
#         "child3" : {
#             "name" : "Emil",
#             "year" : 2004
#         },
#         "child4" : {
#             "name" : "Emil",
#             "year" : 2004
#         },
# }

# print(myFamily)


# ------------------------------------------

# List Items

# List items are ordered, changeable, and allow duplicate values.

# ordered
# changeable
# allow duplicate


# ------------------------------------


# -----------------------
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# ordered
# unchangeable
# allow duplicate

# ---------------------



# -------------------------

# A set is a collection which is both unordered and unindexed.

# Sets are written with curly brackets.

# Set items are unordered, unchangeable, and do not allow duplicate values.

# unordered
# unchangeable
# do not allow duplicate

# ----------------------------------------------




# -----------------------------
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# ordered
# changeable
# does not allow duplicates

# -----------------------------

# myset = {"apple", "banana", "cherry"}

# set1 = {"abc", 34, True, 40, "male"}

# print(len(myset))

# print(set1)

# print(type(set1))

# newSet = set(("apple",))

# print(newSet)

# thisSet = {"sd","sadasd","asdas","dsadsa"}
# newSet = ["hello",]

# thisSet.update(newSet)

# print(thisSet)

# thisSet.add("kumar")
# thisSet.add("kumars")

# print(thisSet)

# print("sd" in thisSet)

# for i in thisSet:
#   print(i)

# theList = ["apple", "banana", "cherry"]

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]


# print(theList)

# print(type(theList))

# print(theList[-3:-1])

# if "apple" in theList:
# 	print("Data Hai")

# theList[1] = "Maza"

# thislist[1:3] = ["blackcurrant", "watermelon"]

# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


# thislist.insert(2, "lo")

# print(thislist)

# i = 1
# while (i<=10):
# 	print(i)
# 	i = i+1
# print("for simple interest")
# p=int(input("enter principle Amount:"))
# r=int(input("enter rate of interest:"))
# t=int(input("enter time:") )
# si = (p*r*t/100)

# print("SI is:",si)


# num = 0;
# n1 = 0;
# n2 = 1;
# print(n1)
# print(n2)
# while num<10:
# 	n3 = n2 + n1;
# 	print(n3);
# 	n1 = n2;
# 	n2 = n3;
# 	num = num + 1;

# import socket
# s = socket.socket()
# print('socket Created')

# s.bind(('localhost',9999))
# s.listen(3)

# print('waiting for connection')

# while True:
# 	c, addr = s.accept()
# 	name = c.recv(1024).decode()
# 	print("Connected with ", addr, name)
# 	c.send(bytes("Welcome to Kumar", 'utf-8'))
# 	c.close()

# import datetime
# import json

# print(datetime.datetime.now)

# a = 5
# b = 6

# if a and b == 5:
#   print("Hello")
# else:
#   print("Hi")


# x =  '{ "name":     true, "age":30, "city":"New York"}'


# print(x)

# import stripe
# stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


# charge = stripe.Charge.retrieve(
#   "ch_3Jcbsc2eZvKYlo2C0erz8wZl",
#   api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
# )
# charge.save() # Uses the same API Key.


# import stripe
# stripe.api_key = "sk_test_4NBbDxxVc50ogIZOEARYRKNP00AnsXYzDi"

# # `source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
# final = stripe.Charge.create(
#   amount=2000,
#   currency="inr",
#   source="tok_amex",
#   description="My First Test Charge (created for API docs)",
# )

# print(final)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]


# print(thislist)

# thislist.sort()

# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# print(thislist)

# thislist.sort()

# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# print(thislist)

# thislist.sort(reverse=True)

# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# Python program for implementation of Bubble Sort

# def bubbleSort(arr):
# 	n = len(arr)
# 	for i in range(n-1):
# 		for j in range(0, n-i-1):
# 			if arr[j] > arr[j + 1] :
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# arr = [64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
# 	print ("% d" % arr[i]),

# newlist = [expression for item in iterable if condition == True]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# exit()

# list1 = [1]

# list2 = ["Hello","Hello","Hello","Hello","Hello","Hello"]


# list2.remove("Hello")

# print(list2)

# exit()



# print(list2.count("Hello"))

# exit()

# list1.extend(list2)

# print(list1)

# exit()



# for x in list2:
# 	list1.append(x)


# print(list1)

# exit()

# print(list1+list2)

# exit()

# thislist = ["banana", "Orange", "Kiwi", "cherry"]


# mylist = thislist.copy()

# mylist = list(thislist)

# print(mylist)

# exit()

# thislist.sort(key = str.lower )
# thislist.reverse()


# print(thislist)


# def bubbleSort(arr):
# 	n = len(arr)
# 	# print(n)

# 	for i in range(n-1):
# 		#print(i)
# 		for j in range(0,n-i-1):
# 			#print(j, end="")
# 			if arr[j] > arr[j + 1] :
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)

# print(arr)




# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "D:\\myfiles\welcome.txt"

# f = open("demofile1.txt",'a')

# print(f.read(55))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readline())
# f.close()
# for x in f:
# 	print(x)

# f.write("Hello Kumar")



# f = open("demofile.text","a")

# f.write("Hello This is Python Class")

# f.close()


# f = open("demofile.text","r")

# print(f.read())
# f.close()


# f = open("demofile.txt", "x")

# import os

# # os.remove("demofile.txt")

# if os.path.exists("demofile.txt"):
# 	print("File Hai")
# else:
# 	print("File Nahi Hai")


# os.rmdir("myfolder")



# number = 5

# # print(number)
# sumOfNumber = 0
# for x in range(1,11):
# 	sumOfNumber = sumOfNumber+x;
# print(sumOfNumber)
# import cgitb

# print ("Content-Type : text/html")

# # then comes the rest hyper-text documents
# print ("<html>")
# print ("<head>")
# print ("<title>My First CGI-Program </title>")
# print ("<head>")
# print ("<body>")
# print ("<h3>This is HTML's Body section </h3>")
# print ("</body>")
# print ("</html>")


# f = open("newText.txt",'a')


# f.write("Hello This is Python Class")



# f.close()

# def my_function(fname=""):
# 	print("Hello "+fname+" "+ "Kumar")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:


# def sumOfNumber(*numbers):
# 	print(numbers)


# sumOfNumber(5,6,7)


# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.


# def my_function(**kid):
#   print(kid)


# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# def my_function(listT):
# 	for x in listT:
# 		print(x)


# listT = ["Sharvan","Kumar","Raushan","Rahul"]

# my_function(listT)


# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def myfunction():
#   pass

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1) # 10 + 9 + 8 + 7 +
#     #print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# print(tri_recursion(10))

# x = lambda a : a + 10


# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# x = "global"

# def foo():
# 	print("inside The Fynction", x)


# foo()

# print(x)

# x = "global"

# def foo():
#     x = x * 2
#     print(x)

# foo()


# def foo():
#     y = "local"
#     print(y)


# foo()

# x = "global"

# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)

# foo()


# x = 5

# def foo():
#     x = 10
#     print("local x:", x)


# foo()
# print("global x:", x)

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()

# key = ('Point_ID', 'Easting', 'Northing', 'Elevation', 'Feature_code', 'Bearing,Bearing_deg', 'Direction', 'Deflection_Angle','Deflection_Angle_deg', 'chain_cal','slope_deg')

# t = ('TP0', '289964.4471', '2400143.593', '17.872', 'TP', 167.40594616616244, "167 °, 24', 21.4''", '', '', '', 0.0, -77.40594616616242)


# # dictionary = {}
# # for x in t:
# # 	for y in range(0,len(key)-1):
# #     	#dictionary.setdefault(key[y], []).append(x)
# #     	print(x)


# # print(dictionary)
# # exit()

# # for x in t:
# # 	for y in range(0,len(key)-1):
# # 		print(y)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# # mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(dictionary)


# exit()

# people = [
# {'name': "Tom", 'age': 10},
# {'name': "Mark", 'age': 5},
# {'name': "Pam", 'age': 7}
# ]

# for x in range(len(people)):
# 	print(people[x])





# exit()

# dictionary = {}
# for idx, x in enumerate(key):
#     	dictionary.setdefault(x, ''.join([])).append(t[idx])


# print(dictionary)
# exit()
# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# # mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(dictionary)



# exit()
# # Python code to convert into dictionary

# def Convert(tup, di):
#     for a, b in tup:
#         di.setdefault(a, []).append(b)
#     return di

# # Driver Code
# tups = [('TP0', '289964.4471'), ('289964.4471', '289964.4471')]
# dictionary = {}
# # print (Convert(tups, dictionary))

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(Convert(tups, dictionary))


import datetime

datetime_object = datetime.datetime.now() #Get Current Date and Time

# print(datetime_object)

# print(datetime.date.today())  #Get Current Date

# print(dir(datetime)) #We can use dir() function to get a list containing all attributes of a module.


# Commonly used classes in the datetime module are:

# date Class
# time Class
# datetime Class
# timedelta Class

# d = datetime.date(2021,9,9)

# print(d)

from datetime import date

# d = datetime.date(2021,9,9)

# print(d)

# print("Current Date : ", date.today())

# print(date.fromtimestamp(1326244364))
# today = date.today()
# print(today)

# print(today.year)
# print(today.month)
# print(today.day)


from datetime import time

# a = time(11,34,56)

# print(a.hour)
# print(a.minute)
# print(a.second)

# print(a)



from datetime import datetime, date

# a = datetime(2018,11,11, 23, 55, 59, 342380)

# print(a)



# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)

# print("timestamp =", a.timestamp())


# t1 = date(2021, 9, 26)
# t2 = date(2021, 8, 26)

# t3 = t1-t2

# print(t3)

# t4 = datetime(year = 2021, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5


# print("t6 =", t6)
# print("type of t3 =", type(t3)) 
# print("type of t6 =", type(t6))  



from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

# t3 = t1 - t2

# print(t3)


# t1 = timedelta(seconds = 33)
# t2 = timedelta(seconds = 54)
# t3 = t1 - t2

# print("t3 =", t3)
# print("t3 =", abs(t3))


# t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
# print("total seconds =", t.total_seconds())


# now = datetime.now()

# s1 = now.strftime("%d/%m/%Y, %H:%M:%S")


# print("time:", s1)


# date_string = "21 June, 2018"
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# import pytz

# local = datetime.now()

# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_NY = pytz.timezone('America/New_York') 
# datetime_NY = datetime.now(tz_NY)
# print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))



# import threading 
  
# def print_hello_three_times():
#   for i in range(3):
#     print("Hello")
  
# def print_hi_three_times(): 
#     for i in range(3): 
#       print("Hi") 

# t1 = threading.Thread(target=print_hello_three_times)  
# t2 = threading.Thread(target=print_hi_three_times)  

# t1.start()
# t2.start()


# import threading 
# import time
  
# def print_hello():
#   for i in range(4):
#     time.sleep(5)
#     print("Hello")
  
# def print_hi(): 
#     for i in range(4): 
#       time.sleep(1)
#       print("Hi") 

# t1 = threading.Thread(target=print_hello)  
# t2 = threading.Thread(target=print_hi)  
# t1.start()
# t2.start()


# Basic method of setting and getting attributes in Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()


# Set the temperature
human.temperature = 37


# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())
