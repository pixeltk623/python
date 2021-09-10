import datetime

x = datetime.datetime.now()
print(x)

# o/p = 2021-09-10 08:42:34.886114

# Date Output
# When we execute the code from the example above the result will be:

# 2021-09-10 08:42:01.179492
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))



# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

x = datetime.datetime(2020, 5, 17)

print(x)

# 2020-05-17 00:00:00

# The datetime() class also takes parameters for time and timezone 
#(hour, minute, second, microsecond, tzone), but they are optional, 
#and has a default value of 0, (None for timezone).

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# June

# Python Math
# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)


# The pow(x, y) function returns the value of x to the power of y (xy).


x = pow(4, 3)

print(x)


# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

import math

x = math.sqrt(64)

print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


x = math.pi

print(x)
