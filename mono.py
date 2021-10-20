
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)


thisDict = {
		"brand": "Ford",
  		"model": "Mustang",
  		"year": 1964,
  		 "colors": ["red", "white", "blue"]
	}



for x in thisDict.items():
  print(x)



# del thisDict["model"]
# print(thisDict)


# thisDict.popitem()

# thisDict.pop("model")
# print(thisDict)


exit()
thisDict.update({"location": "patna"})

print(thisDict)

exit()

print("brand" in thisDict)

x = thisDict.items()

#The items() method will return each item in a dictionary, as tuples in a list.



print(x)

exit()

print(thisDict.keys())
print(thisDict.values())

print(len(thisDict))
print(thisDict)

exit()
# set1 = {"asdas","asdas","asdas","asdas","asdas","asdas"}
# set2 = {"address","asdas","asdas","asdas","asdas","asdas","asdas"}

# set3 = set1.union(set2)

# print(set3)

# set1.update(set2)

# print(set1)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)

# z = x.intersection(y)

# print(z)

# x.symmetric_difference_update(y)

# print(x)

# z = x.symmetric_difference(y)

# print(z)

# exit()
# The union() method returns a new set with all items from both sets:

# The intersection_update() method will keep only the items that are present in both sets.

# set1 = {2, "b" , "c"}
# set2 = {1, 2, 3}


# set3 = set1.intersection_update(set2)

# print(set3)

# exit()

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mylist = [
#   { "name": "Python New", "address": "baroda st 652"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:

# print(x.inserted_ids)


#Tuple items are ordered, unchangeable, and allow duplicate values.

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)


# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)


# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)



# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)


# exit()


#Set items are unordered, unchangeable, and do not allow duplicate values.

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.


# Note: If the item to remove does not exist, discard() will NOT raise an error.




# exit()

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# mylist = ("kiwi", "orange")

# thisset.update(mylist)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}


# thisset.add("asdas")

# print(thisset)

# exit()
# print("apple" in thisset)

# for x in thisset:
#   print(x)

# exit()

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)


# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))


# exit()


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)



# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# exit()

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# exit()

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)


# print(thistuple)

# #Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# exit()

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")






# exit()

# thistuple = ("apple", "banana", "cherry")
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))



# print(len(thistuple))


# print(thistuple)