from datetime import datetime
from threading import Timer
# import schedule

x=datetime.today()
y=x.replace(minute=41)
if y==x:
    print(x)
    print("It is time")
    print(y)
else:
    print(x)
    print("The time has not reached")