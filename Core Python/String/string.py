# The Python isalpha() method returns true if a string only contains letters.
# Python isnumeric() returns true if all characters in a string are numbers.
# Python isalnum() only returns true if a string contains alphanumeric characters, without symbols.

# string_name = "ThisisKumar";

# print(string_name.isalpha())

# first_name = input("What is your first name?")
# second_name = input("What is your second name?")

# print(first_name.isalpha())
# print(second_name.isalpha())

# string_name.isnumeric()

# student_answer = input("What is 9 x 10?")

# print(student_answer.isnumeric())


# username = input("Choose a username:")

# if username.isalnum() == True:
# 	print("Your new username is ", username)
# else:
# 	print("This username is invalid.")


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
exit()


txt = "bananaass"

x = txt.center(11, "O")

print(x)



a = "Kumar"

print(a.capitalize())

txt = "Hello, And Welcome To My World!"

x = txt.lower()

print(x)


exit()
a = """Lorem Ipsum is simply dummy 
text of the printing and typesetting 
industry. Lorem Ipsum has been the industry 
standard dummy text ever since the 1500s,
when an unknown printer took a galley of
type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also
the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum.
"""

txt = "We are the so-called \"Vikings\" from the north."
print(txt)



a = "Hello Sharvan"

a = "Hello, World!"

age = 36
txt = "My name is Sharvan , I am {}."

print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


exit()

print(a.split(","))

print(a.replace("Hello","Kumar"))

exit()
print(a.upper())
print(a.lower())
print(a.strip())

exit()

print(a[-5:-2])

exit()
print("expensive" not in a)


print( "Hello" in a )

print(len(a))
# for x in a:
# 	print(x)



