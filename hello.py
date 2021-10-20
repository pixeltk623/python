# a = int(input("Enter The Number"))
# sum = 0

# while(a!=0):
#     r = a%10
#     sum = sum + r
#     a = int (a/10)

# print(sum)


# a = 11
# cont = 0
# for i in range(1, a+1):
#     if a%i==0:
#         cont = int(cont) + 1

# if cont==2:
#     print("Prime No")
# else:
#     print("Not Prime")

# sum = 0
# for i in range(1,11):
#     if i%2==0:
#         sum = sum + i
#     # else:
#     #     sumE = sumE + i
# # print(sumE)
# print(sum)



# import speedtest
# wifi  = speedtest.Speedtest()
# print("Wifi Download Speed is ", wifi.download())
# print("Wifi Upload Speed is ", wifi.upload())


# print("Hello This is Kummar")


# import datetime

# x = datetime.datetime.now()

# print(x)
# print(x.year)
# print(x.month)
# print(x.day)

# print(x.strftime("%A"))

# y = datetime.datetime(2020,5,17,14,50,50)

# print(y)


# for x in range(1,10):
# 	for y in range(1,x):
# 		print("*",end="")
# 	print("\r")


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle

# n=5
# k = n - 1 # 4 
# for i in range(0, n):
# 	for j in range(0, k):
# 		print(end=" ")
# 	k = k - 1
# 	for j in range(0, i+1):
# 		print("* ", end="")
# 	print("\r")

# myList = ["Test","Hello", "No"]

# print(myList)


# # Importing the OpenCV library
# import cv2
# # Reading the image using imread() function
# image = cv2.imread('image.png')

# # Extracting the height and width of an image
# h, w = image.shape[:2]
# # Displaying the height and width
# print("Height = {}, Width = {}".format(h, w))

# # Extracting RGB values.
# # Here we have randomly chosen a pixel
# # by passing in 100, 100 for height and width.
# (B, G, R) = image[100, 100]

# # Displaying the pixel values
# print("R = {}, G = {}, B = {}".format(R, G, B))

# # We can also pass the channel to extract
# # the value for a specific channel
# B = image[100, 100, 0]
# print("B = {}".format(B))

# roi = image[100 : 500, 200 : 700]

# print(roi)

# Python code to read image
# import cv2

# # To read image from disk, we use
# # cv2.imread function, in below method,
# img = cv2.imread("image.png", cv2.IMREAD_COLOR)

# # Creating GUI window to display an image on screen
# # first Parameter is windows title (should be in string format)
# # Second Parameter is image array
# cv2.imshow("Cute Kitens", img)

# # To hold the window on screen, we use cv2.waitKey method
# # Once it detected the close input, it will release the control
# # To the next line
# # First Parameter is for holding screen for specified milliseconds
# # It should be positive integer. If 0 pass an parameter, then it will
# # hold the screen until user close it.
# cv2.waitKey(0)

# # It is for removing/deleting created GUI window from screen
# # and memory
# cv2.destroyAllWindows()


# import re

# pattern = '^a...s$'
# test_string = 'aliasasdas'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	


# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()



# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)