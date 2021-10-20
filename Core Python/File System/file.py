#f = open("test.txt", "r")



# for file in f:

# 	print(file)
	


# print(f.read(10))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f = open("test.txt", "w")

# f.write("This is New Para")
# f.write("This is New Para")
# f.write("This is New Para")


# f = open("test.txt", "a")

# f.write("This is New append File")

# f = open("test.txt", "r")

# print(f.read())

# f = open("test.txt", "a")


# f.write("New Para")

# f = open("test.txt", "r")

# print(f.read())

# f.close()



# Python3 program to demonstrate the use of
# rstrip() method using optional parameters
 
# string which is to be stripped
# string = "geekssss"

# string_new = "sssgeek"
 
# # Removes given set of characters from
# # right.
# # print(string.rstrip('s'))

# # print(string_new.lstrip('s'))


# for string in string:
# 	pass


# Python3 program to demonstrate the use of
# strip() method 
 
# string = """    geeks for geeks    """


 
# # prints the string without stripping
# print(string)	
 
# # prints the string by removing leading and trailing whitespaces
# print(string.strip())  
 
# # prints the string by removing geeks
# print(string.strip(' geeks'))

# newString = "Tops Tech"

# print(newString.strip(" Tech"))

# txt = "Test"

# x = txt.index("e")
# x = txt.replace("e","")

# print(x)

# a_string = "abcde"

# sliced = a_string[2:]

# print(sliced)

# Python code to illustrate split() function
# with open("test.txt", "r") as file:
# 	data = file.readlines()
# 	#print(data)
# 	for line in data:
# 		word = line.split()
# 		print (word)

# file1 = open("test.txt", "w")
# L = ["This is Delhi", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()


# txt = 'It\'s alright.'
# print(txt) 


# import os
# os.remove("remove.txt")

import os
if os.path.exists("remove.txt"):
  os.remove("remove.txt")
else:
  print("The file does not exist")