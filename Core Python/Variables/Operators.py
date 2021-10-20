

# Python 3 code to demonstrate 
# removing duplicated from list 
# using naive methods 
  
# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# print ("The original list is : " +  str(test_list))
  
# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
# print ("The list after removing duplicates : " + str(res))


users = ["sharvan","sanjeev","sanjeev","sanjeev","sanjeev","sharvan"]

#count = 0
dictT = []
for u in users:
	count = 0
	for x in range(6):
		if u in users[x]:
			count += 1

	dictT.append({u: count})
	count = 0


#print(dictT)
res = []
for i in dictT:
    if i not in res:
        res.append(i)

print(res)
exit()


x = 5
#x += 5 # x = x + 5
x **= 5	
#x = x - 5


print(x)


exit()

# Arithmetic operators

x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)


# Comparison operators
# Comparison operators are used to compare values. It returns either True or False according to the condition.

x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

# Logical operators

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

# Assignment operators

# Assignment operators are used in Python to assign values to variables.

# a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

# There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.




# Special operators
# Python language offers some special types of operators like the identity operator or the membership operator. They are described below with examples.

# Identity operators
# is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.


# Operator	Meaning	Example
# is	True if the operands are identical (refer to the same object)	x is True
# is not	True if the operands are not identical (do not refer to the same object)	x is not True



# Identity operators in Python


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'


x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


# But x3 and y3 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.


# Membership operators
# in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

# In a dictionary we can only test for presence of key, not the value.

# Operator	Meaning	Example
# in	True if value/variable is found in the sequence	5 in x
# not in	True if value/variable is not found in the sequence	5 not in x


# Membership operators in Python


x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

x = 8
x = x // 5
#the floor division // rounds the result down to the nearest whole number


print(x)


# Python Keywords

# Keywords are the reserved words in Python.

# We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language.

# In Python, keywords are case sensitive.

# There are 33 keywords in Python 3.7. This number can vary slightly over the course of time.

# All the keywords except True, False and None are in lowercase and they must be written as they are. The list of all the keywords is given below.


# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield
