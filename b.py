
# my_list = [12, 65, 54, 39, 102, 339, 221,]

# result = list(filter(lambda x: (x % 13 == 0), my_list))

# print("Numbers divisible by 13 are",result)

def fun(variable):
	letters = ['a', 'r', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
print('The filtered letters are:')
for s in filtered:
	print(s)

exit()
# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# # with dictionary
# print(Counter({'A':3, 'B':5, 'C':2}))

# # with keyword arguments
# print(Counter(A=3, B=5, C=2))


#exit()

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# myset = {"apple", "banana", "cherry"}
# myset = {"apple", "banana", "cherry","apple", "banana", "cherry"}

# # myset = {}

# myset = {"asa",True,True}

# print(len(myset))

# print(type(myset))

# print(myset)



# thisSet = set(("asdsa",))

# print(thisSet)

# thisset = {"apple", "banana", "cherry"}


# # print(thisset)

# for x in thisset:
# 	print(x)


# print("Apple" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.

# thisset.add("orange")
# thisset.add("apple")

# thisset.update({"orange"})
# thisset.update(["orange1"])
# thisset.update(("orange2",))

# print(thisset)


# thisset.remove("banana1")
# thisset.discard("banana")

# thisset.pop()
# thisset.pop()
# thisset.pop()

# print(thisset)

# x = thisset.pop()

# print(x)

# print(thisset)

# thisset.clear()

# del thisset

# print(thisset)

# for x in thisset:
# 	print(x)
	

# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() 
# method that inserts all the items from one set into another:



s1 = {2,"b","c"}
s2 = {1,2,3}

# s3 = s1.union(s2)

# s1.update(s2)

# print(s3)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# s1.intersection_update(s2)

# print(s1)

# s2.intersection_update(s1)

# print(s2)

# The intersection() method will return a new set, that only contains the items
# that are present in both sets.

# s3 = s1.intersection(s2)

# print(s3)


# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT
# present in both sets.

# s1.symmetric_difference_update(s2)

# print(s1)

# s3 = s1.symmetric_difference(s2)

# print(s3)





































# exit()
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'ACcf617ef07f0b303abb37a1746cce8615'
# auth_token = 'a41e4449187ca561de5f3ce802fa9cac'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18788776105',
#                      to='+918160410477'
#                  )

# print(message.sid)

# exit()


# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'ACcf617ef07f0b303abb37a1746cce8615'
# auth_token = 'a41e4449187ca561de5f3ce802fa9cac'
# client = Client(account_sid, auth_token)


# calls = client.calls.list(limit=20)

# print(calls)

# for record in calls:
#     print(record.sid)



# # for x in range(1,10):
# # 	print(x)

# exit()

	


# # def sort(listOfArray):

# #     for i in range(len(listOfArray)-1,0,-1):

# #         for j in range(i):

# #             if listOfArray[j]>listOfArray[j+1]:
# #                 temp = listOfArray[j]
# #                 listOfArray[j] = listOfArray[j+1]
# #                 listOfArray[j+1] = temp

# # nums = [5,3,8,6,7,2]

# # sort(nums)

# # print(nums)

# # # print(sorted(nums))

# sumofN = 0
# for x in range(1,11):
# 	# print(x)
# 	#sumofN = sumofN + x # 0 + 1 = 1 2 3

# 	if x%2==0:
# 		#print(x)
# 		sumofN = sumofN+x;

# print(sumofN)
