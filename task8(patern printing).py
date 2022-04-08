"""
To take input for number of rows
To take binary input and typecast into boolean True or False

If true and n = 4, then print
*
**
***
****

if false and n=4, then print
****
***
**
*
"""

a = int(input("Enter your number:\n"))
b = int(input("Choose between 1 and 0\n"))
c = bool(b)
if c==True:
    for i in range (0,a):
        for j in range (0,i+1):
            print("*", end="")
        print()
elif c==False:
    for i in range(0,a):
        for j in range(0,a-i):
            print("*", end="")
        print()