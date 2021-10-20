import threading
import time


def print_time(tname, delay):
	count = 0

	while count<5:
		time.sleep(delay)
		count += 1
		print ("%s: %s" % ( tname, time.ctime(time.time()) ))


# Create two threads as follows
try:
   t1 = threading.Thread(target=print_time, args=("Thread-1", 4,))
   t2 = threading.Thread(target=print_time, args=("Thread-2", 10,))

   t1.start()
   t2.start()

   # t1 = threading.Thread(target=print_square, args=(10,))
   # t2 = threading.Thread(target=print_cube, args=(10,))
except:
   print("Error: unable to start thread")

while 1:
   pass
