# A tuple in Python is similar to a list. 
# The difference between the two is that we cannot change the elements 
# of a tuple once it is assigned whereas we can change the elements of a list.

# myTuple = ()

# print(myTuple)

# my_tuple = (1, 2, 3)
# print(my_tuple)

# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# # nested tuple
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)


# # A tuple can also be created without using parentheses. This is known as tuple packing.

# my_tuple = 3, 4.6, "dog"
# # print(my_tuple)

# # tuple unpacking is also possible
# a, b, c = my_tuple

# print(a)      # 3
# print(b)      # 4.6
# print(c)      # dog


# my_tuple = ("hello")
# print(type(my_tuple))  # <class 'str'>

# # Creating a tuple having one element
# my_tuple = ("hello",)
# print(type(my_tuple))  # <class 'tuple'>

# # Parentheses is optional
# my_tuple = "hello"
# print(type(my_tuple))  # <class 'tuple'>


# Access Tuple Elements
# There are various ways in which we can access the elements of a tuple.

# 1. Indexing
# We can use the index operator [] to access an item in a tuple, where the index starts from 0.

# So, a tuple having 6 elements will have indices from 0 to 5. Trying to access an index outside of the tuple index range(6,7,... in this example) will raise an IndexError.

# The index must be an integer, so we cannot use float or other types. This will result in TypeError.

# Likewise, nested tuples are accessed using nested indexing, as shown in the example below.


# my_tuple = ('p','e','r','m','i','t')


# print(my_tuple[0])

# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))


# print(n_tuple)

# # nested index
# print(n_tuple[0][3])       # 's'
# print(n_tuple[1][1])       #  4



# 2. Negative Indexing
# Python allows negative indexing for its sequences.

# The index of -1 refers to the last item, -2 to the second last item and so on.

# Negative indexing for accessing tuple elements
# my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# # Output: 't'
# print(my_tuple[-1])

# # Output: 'p'
# print(my_tuple[-6])


# 3. Slicing
# We can access a range of items in a tuple by using the slicing operator colon 




# # Accessing tuple elements using slicing
# my_tuple = ('p','r','o','g','r','a','m','i','z')

# # elements 2nd to 4th
# # Output: ('r', 'o', 'g')
# print(my_tuple[1:4])

# # elements beginning to 2nd
# # Output: ('p', 'r')
# print(my_tuple[:-7])

# # elements 8th to end
# # Output: ('i', 'z')
# print(my_tuple[7:])

# # elements beginning to end
# # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# print(my_tuple[:])



# Changing a Tuple
# Unlike lists, tuples are immutable.

# This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like a list, its nested items can be changed.

# We can also assign a tuple to different values (reassignment).


# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# my_tuple[1] = 9

# print(my_tuple)


# However, item of mutable element can be changed
# my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
# print(my_tuple)

# my_tuple = ('p','r','o','g','r','a','m','i','z')

# # Tuples can be reassigned
# my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# print(my_tuple)


# We can use + operator to combine two tuples. This is called concatenation.

# We can also repeat the elements in a tuple for a given number of times using the * operator.

# Both + and * operations result in a new tuple.


# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)



# # Deleting tuples
# my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# # can't delete items
# # TypeError: 'tuple' object doesn't support item deletion
# # del my_tuple[3]

# # Can delete an entire tuple
# del my_tuple

# # NameError: name 'my_tuple' is not defined
# print(my_tuple)



my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3


# Other Tuple Operations
# 1. Tuple Membership Test
# We can test if an item exists in a tuple or not, using the keyword in.


# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)


# 2. Iterating Through a Tuple
# We can use a for loop to iterate through each item in a tuple.


# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)


# Advantages of Tuple over List
# Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
