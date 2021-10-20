# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.


# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x, indent=4))
json.dumps(x, indent=4, sort_keys=True)

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# json.dumps(x, indent=4, separators=(". ", " = "))

# json.dumps(x, indent=4, sort_keys=True)


# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern. For example,

# ^a...s$

# The above code defines a RegEx pattern. The pattern is: any five letter string starting with a and ending with s.

import re

pattern = '^a...s$'
test_string = 'ahars'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")


#   specify Pattern Using RegEx
# To specify regular expressions, metacharacters are used. In the above example, ^ and $ are metacharacters.

# MetaCharacters
# Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

# [] . ^ $ * + ? {} () \ |

# [] - Square brackets

# Square brackets specifies a set of characters you wish to match.

# [abc]
# a 1 match
# ac  2 matches
# Hey Jude  No match
# abc de ca 5 matches


# Here, [abc] will match if the string you are trying to match contains any of the a, b or c.

# You can also specify a range of characters using - inside square brackets.

# [a-e] is the same as [abcde].
# [1-4] is the same as [1234].
# [0-39] is the same as [01239].
# You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

# [^abc] means any character except a or b or c.
# [^0-9] means any non-digit character.



#--------------------------------------------


# Python RegEx
# Python has a module named re to work with regular expressions. To use it, we need to import the module.

# re.findall()
# The re.findall() method returns a list of strings containing all matches.


# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']

# If the pattern is not found, re.findall() returns an empty list.

# re.split()
# The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.

# \d - Matches any decimal digit. Equivalent to [0-9]



import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


# You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.



import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']



# re.sub()
# The syntax of re.sub() is:

# re.sub(pattern, replace, string)
# The method returns a string where matched occurrences are replaced with the content of replace variable.


# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456


# You can pass count as a fourth parameter to the re.sub() method. If omited, it results to 0. This will replace all occurrences.

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1) 
print(new_string)

# Output:
# abc12de 23
# f45 6

# re.subn()
# The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.


# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)

# Output: ('abc12de23f456', 4)


# re.search()
# The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

# If the search is successful, re.search() returns a match object; if not, it returns None

# match = re.search(pattern, str)

