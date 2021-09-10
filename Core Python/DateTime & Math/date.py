import datetime

from datetime import date


from datetime import time

from datetime import datetime

from datetime import datetime, date
from datetime import timedelta
import pytz
import time

import math


import speedtest

# x = datetime.datetime.now()

# print(x) # current date and Time

# print(x.year)
# print(x.strftime("%A"))


# #oldDate = 2020, 5, 17

# x = datetime.datetime(2021, 8, 11)

# print(x)

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%B"))


# datetime_object = datetime.datetime.today()

# print(datetime_object)

# datetime = dir(datetime)

# print(datetime)

# timestamp = date.fromtimestamp(1631253990)

# a = date(2019, 4, 13)

# print(a);

# print(timestamp)



# date object of today's date
# today = date.today() 
# print(today)
# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)



# a = time(hour = 10, minute = 0, second = 0, microsecond = 5466)
# # a = time()
# print("a =", a)

# datetime()
# a = datetime(2017, 11, 28, 23, 55, 59, 342380)

# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("timestamp =", a.timestamp())
# print(a)

# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("t3 =", t3)


# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)


# print("type of t3 =", type(t3)) 
# print("type of t6 =", type(t6))



# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
# t3 = t1 - t2

# print(t3)


# now = datetime.now()

# t = now.strftime("%H:%M:%S")
# print("time:", t)

# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("s1:", s1)

# s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s2:", s2)

# s3 = now.strftime("%d-%m-%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("s3:", s3)



# date_string = "21 June, 2018"

# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# local = datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_NY = pytz.timezone('Europe/London') 

# # print(tz_NY)
# datetime_NY = datetime.now(tz_NY)

# # print(datetime_NY)

# print("London:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

# now = datetime.now() 
# year = now.strftime("%Y")
# print("year:", year)


# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# timestamp = 1528797322
# date_time = datetime.fromtimestamp(timestamp)

# d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
# print("Output 2:", d)	


# d = date_time.strftime("%I%p")
# print("Output 5:", d)


# print("Printed immediately.")
# time.sleep(5)
# print("Printed after 2.4 seconds.")

# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   time.sleep(1)


# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result, end="", flush=True)
#   print("\r", end="", flush=True)
#   time.sleep(2)

#Three lines to make our compiler able to draw:


# a = 10
# b = 20

# print("The value of a is {} and b is {}".format(a,b))


# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)

# print(y)
# x = abs(-7.25)

# print(x)


# x = pow(4, 3)

# print(x)

# x = math.sqrt(64)

# print(x)

st = speedtest.Speedtest()

# option = int(input('''What speed do you want to test:

# 1) Download Speed

# 2) Upload Speed

# 3) Ping

# Your Choice: '''))


# if option == 1:

# 	print(st.download())

# elif option == 2:

# 	print(st.upload())

# elif option == 3:

# 	servernames =[]

# 	st.get_servers(servernames)

# 	print(st.results.ping)

# else:

# 	print("Please enter the correct choice !")

# startTime = time.process_time()
# d = st.download()
# endTime = time.process_time()

# print(start)

# start = time.process_time()
# # # your code here  
# d = st.download()  
# print(time.process_time() - start)


# start = datetime.now()
# d = st.download() 
# end = datetime.now()
# time_taken = end - start
# print('Time: ',time_taken) 