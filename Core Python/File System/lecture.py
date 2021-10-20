# open() function
# “ r “, for reading.
# “ w “, for writing.
# “ a “, for appending.
# “ r+ “, for both reading and writing



# a file named "test", will be opened with the reading mode.

# This will print every line one by one in the file


# file = open('test.txt', 'r')

# for each in file:
# 	print (each)


# read() mode

# Python code to illustrate read() mode
# file = open("test.txt", "r")
# # print (file.read())

# print (file.read(5))


# write() mode

# Python code to create a file
# file = open('test.txt','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()


# append() mode


# Python code to illustrate append() mode
# file = open('test.txt','a')
# file.write("This will add this line")
# file.close()

# rstrip(): This function strips each line of a file off spaces from the right-hand side.
# lstrip(): This function strips each line of a file off spaces from the left-hand side.


# Python code to illustrate with()
# with open("test.txt") as file:
# 	data = file.read()

# 	print(data)

# do something with data


# split() using file handling

#We can also split lines using file handling in Python. This splits the variable when space is encountered. You can also split using any characters as we wish. Here is the code:

# Python code to illustrate split() function
# with open("test.txt", "r") as file:
# 	data = file.readlines()
# 	for line in data:
# 		word = line.split()
# 		print (word)

# Python append to a file

# Append Only (‘a’): Open the file for writing. The file is created if it does not exist.
#The handle is positioned at the end of the file. The data being written will be inserted at 
#the end, after the existing data.
# Append and Read (‘a+’): Open the file for reading and writing.
#The file is created if it does not exist. 
#The handle is positioned at the end of the file. The data being written will be inserted at 
#the end, after the existing data.

# Python program to illustrate
# Append vs write mode
# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()


# # Append-adds at last
# file1 = open("myfile.txt", "a") # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()

# # Write-Overwrites
# file1 = open("myfile.txt", "w") # write mode
# file1.write("Tomorrow \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()



# Program to show various ways to
# append data to a file using
# with statement

# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# # Writing to file
# with open("myfile.txt", "w") as file1:
# 	# Writing data to a file
# 	file1.write("Hello \n")
# 	file1.writelines(L)

# # Appending to file
# with open("myfile.txt", 'a') as file1:
# 	file1.write("Today")


# # Reading from file
# with open("myfile.txt", "r+") as file1:
# 	# Reading form a file
# 	print(file1.read())



# import os


# os.remove("myfile.txt")

# os.rmdir("")


import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

