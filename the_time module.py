"""
If there is a requirement to know the time pc took to execute, that could be done by the below code.
There is no run time difference between for and while loop but even minute situations can alter the timings
like cpu temperature, daemons running, unnecessary line of codes, etc.
"""
import time

i = 0
sec = time.time()

while i<50:
    print("While loop")
    i += 1

while_loop = time.time() - sec
print("While loop ran in ", while_loop)

for i in range (50):
    print("For loop")

sec2 = time.time()
for_loop = time.time() - sec2
print("For loop ran in ", for_loop)