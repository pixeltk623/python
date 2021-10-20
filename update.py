# import config

# config.a = 10
# config.b = "alphabet"

# Python program to test
# internet speed

# import speedtest


# st = speedtest.Speedtest()

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


# import datetime
# import time
# d = datetime.datetime.now()

# print(d)


# now = datetime.datetime.now()

# t = now.strftime("%Y/%m/%d")

# print(t)

# date = datetime.datetime(2003,8,1,12,4,5)
# for i in range(5): 
#     date += datetime.timedelta(days=1)
#     print(date) 

from datetime import datetime,timedelta
import time

def last_day(d, day_name):
    days_of_week = ['sunday','monday','tuesday','wednesday',
                        'thursday','friday','saturday']
    target_day = days_of_week.index(day_name.lower())
    delta_day = target_day - d.isoweekday()
    if delta_day >= 0: delta_day -= 7 # go back 7 days
    return d + timedelta(days=delta_day)


print(last_day(1,'sunday'))