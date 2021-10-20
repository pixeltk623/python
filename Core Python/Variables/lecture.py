# Example 1: Declaring and assigning value to a variable

website = "apple.com"
print(website)
#Example 2: Changing the value of a variable
website = "apple.com"
print(website)

# assigning a new value to website
website = "abc.com"

print(website)

# Example 3: Assigning multiple values to multiple variables

a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)


x = y = z = "same"

print (x)
print (y)
print (z)


# Constants
# A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.

# You can think of constants as a bag to store some books which cannot be replaced once placed inside the bag.

import constant


print(constant.PI)
print(constant.GRAVITY)


PI = 3.14

PI = 86

print(PI)


# Rules and Naming Convention for Variables and constants
# Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:

# Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:
# snake_case
# MACRO_CASE
# camelCase
# capWords
# Create a name that makes sense. For example, vowel makes more sense than v.
# If you want to create a variable name having two words, use underscore to separate them. For example:
# my_name
# current_salary
# Use capital letters possible to declare a constant. For example:
# PI
# G
# MASS
# SPEED_OF_LIGHT
# TEMP
# Never use special symbols like !, @, #, $, %, etc.
# Don't start a variable name with a digit.


# Literals
# Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

# Numeric Literals
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

# How to use Numeric literals in Python?

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


# String literals
# A string literal is a sequence of characters surrounded by quotes. We can use both single, double, or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# In the above program, This is Python is a string literal and C is a character literal.

# The value in triple-quotes """ assigned to the multiline_str is a multi-line string literal.

# The string u"\u00dcnic\u00f6de" is a Unicode literal which supports characters other than English. In this case, \u00dc represents Ü and \u00f6 represents ö.

# r"raw \n string" is a raw string literal.


# Boolean literals
# A Boolean literal can have any of the two values: True or False.

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Special literals
# Python contains one special literal i.e. None. We use it to specify that the field has not been created.

# How to use special literals in Python?


drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)



# Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

# How to use literals collections in Python?

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)



# Data types in Python
# Every value in Python has a datatype. Since everything is an object in Python programming,
# data types are actually classes and variables are instance (object) of these classes.


# Python Numbers
# Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

# We can use the type() function to know which class a variable or a value belongs to. Similarly, the isinstance() function is used to check if an object belongs to a particular class.

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# Type Conversion
# The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.

# Implicit Type Conversion
# Explicit Type Conversion


# Implicit Type Conversion
# In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

# Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.


num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

# Explicit Type Conversion
# In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.

# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

# Addition of string and integer using explicit conversion

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))



print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

print("\n")

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))


print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))


print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))


# x = 12.3456789
# print('The value of x is %3.2f' %x)

# print('The value of x is %3.4f' %x)
# The value of x is 12.3457

# num = input('Enter a number: ')


# import math

# print(math.pi)


# from math import pi


# pi


print("Hello This is  {} and my father name is {}".format("sharvan","Arun"))