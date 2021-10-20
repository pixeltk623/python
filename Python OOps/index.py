# class MyNewClass:

# 	'''This is a docstring. I have created a new class'''
# 	pass

# class Person:
# 	"This is a person class"
# 	age = 10

# 	def greet(self):
# 		print("Hello")


# # print(Person.age)

# # print(Person.greet)

# # print(Person.__doc__)

# harry = Person()


# harry.greet()


# class ComplexNumber:
#     def __init__(self, r=0, i=0):
#         self.real = r
#         self.imag = i

#     def get_data(self):
#         print(f'{self.real}+{self.imag}j')

# num1 = ComplexNumber(2, 3)

# num1.get_data()


# num2 = ComplexNumber(5)
# num2.attr = 10
# print((num2.real, num2.imag, num2.attr))
# # print(num1.attr)



# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)


# t = Triangle()

# t.inputSides()

# t.dispSides()

# t.findArea()


# Example 1: Creating Class and Object in Python

# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# Example 2 : Creating Methods in Python


# class Parrot:
    
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # instance method
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)

#     def dance(self):
#         return "{} is now dancing".format(self.name)

# # instantiate the object
# blu = Parrot("Blu", 10)

# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())


# Example 3: Use of Inheritance in Python



# parent class
# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()


# Encapsulation
# Using OOP in Python, we can restrict access to methods and variables. 
# This prevents data from direct modification which is called encapsulation.
# In Python, we denote private attributes using underscore as the prefix 
# i.e single _ or double __.

# Example 4: Data Encapsulation in Python


# class Computer:

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()


# Polymorphism
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
# However we could use the same method to color any shape.
# This concept is called Polymorphism.


class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)