# class Person:
# 	"This is Person Class"
# 	age = 10

# 	def greet(self):
# 		print("Hello")


# # print(Person.age)
# # print(Person.greet)

# # print(Person.__doc__)


# harry = Person()

# harry.greet()

class ComplexNumber:
	def __init__(self, r=0, i=0):
		self.real = r
		self.imag = i

	def get_data(self):
		print(f'{self.real}+{self.imag}j')



# num1 = ComplexNumber(2,3)

# num1.get_data()
# num2 = ComplexNumber(5)
# num2.attr = 10

# print((num2.real, num2.imag, num2.attr))

# print(num1.attr)


# print((num2.real, num2.imag, num2.attr))
# print(num1.attr)

#num1 = ComplexNumber(2,3)
# del num1.imag
# num1.get_data()

# del ComplexNumber.get_data
# num1.get_data()