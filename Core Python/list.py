{"target":"run_existing_window_command",
"id":"repl_python_run",
"file":"config/python/Main.sublime-menu"}

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1,n2,n3)


# List
# Lists are used to store multiple items in a single variable.
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# thislist = ["apple", "banana", "cherry"]

# print(thislist[2])

#Allow Duplicates

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)

#List Length

# print(len(thislist))

# List Items - Data Types

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(type(list1))

# print(type(list2))

# print(type(list3))

# list4 = list(["apple", "banana", "cherry"])
# print(list4)

#List Constructor

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

# print(thislist)

# allNumber = [1, 5, 7, 9, 3]

# print(allNumber.count(1))

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-3])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]

# if "applek" in thislist:
# 	print("Hai")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# thislist.insert(1, "asdsa")
# print(thislist)

# Append Items
# To add an item to the end of the list, use the append() method:
# thislist.append("asdadasds")

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# Remove Specified Item
# The remove() method removes the specified item.


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# newlist = [expression for item in iterable if condition == True]


# newlist = [x for x in range(10)]

# print(newlist)

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = ['hello' for x in fruits]

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist = [100, 50, 65, 82, 23]

# # thislist.sort() 

# thislist.sort(reverse = True)
# print(thislist)

# print(thislist)


# def myFun(n):
# 	return abs(n-50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myFun)
# print(thislist)


# list1 = ["cc","a","aaa","eeee","dddddd"]
# print(list1)

# list1.sort(key=len)

# print(list1)

# list2 = [[2,9],[1,10],[3,7]]

# list2.sort()

# def sortByFun(element):
# 	return element[1]

# list2.sort(key=sortByFun)

# print(list2)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# # copyList = thislist.copy()

# copyList = list(thislist)

# print(copyList)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# n_list = ["Happy", [2, 0, 1, 5]]


# print(n_list[1][0])

# print(n_list[0][1])

# print(n_list[1][3])