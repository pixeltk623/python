# 1. Python Program to Find the Largest Among Three Numbers


# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# 2. Python Program to Check Prime Number

# 3. Python Program to Print all Prime Numbers in an Interval

# 4. Python Program to Find the Factorial of a Number
# 5. Python Program to Find the Factorial of a Number

# 6. Python Program to Display the multiplication Table

# Multiplication table (from 1 to 10) in Python

num = 12

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# 7. Python Program to Print the Fibonacci sequence

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# How many terms? 7
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8

# 8. Python Program to Check Armstrong Number

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# 9. Python Program to Find the Sum of Natural Numbers

num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# 10. Python Program to Reverse a Number

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

# 11. Example 1: Calculate power of a number using a while loop


base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
