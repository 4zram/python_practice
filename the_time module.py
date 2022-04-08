"""
If there is a requirement to know the time pc took to execute, that could be done by the below code.
There is no run time difference between for and while loop but even minute situations can alter the timings
like cpu temperature, daemons running, unnecessary line of codes, etc.
"""
import time

i = 0
sec = time.time()   #Time.time() returns the ticks.

while i<3:
    print("While loop")
    time.sleep(2)       # Will pause the program for 2 seconds.
    i += 1

while_loop = time.time() - sec
print("While loop ran in ", while_loop)

sec2 = time.time()

for i in range (3):
    print("For loop")
    time.sleep(2)

for_loop = time.time() - sec2
print("For loop ran in ", for_loop)

# To return the current time, the code would look like this
min = time.asctime(time.localtime(time.time()))
print("Current time is ", min)

"""
time.time() will return the ticks from a certain date to now.
time.loacltime() will convert the time into local time and return in tuple form.
time.asctime() will convert the tuple returned from time.localtime() and return to this presentable format.
"""