# File IO basics
"""
"r" - open file for reading - default
"w" - open file for writing
"x" - create file if not exist
"a" - append more contents to the file
"t" - text mode - default
"b" - binary mode
"+" - read and write (open and update file)
"""

# How to read from a file
j = open("azram.txt")
a = j.read()
print(a)
j.close() # Closing a file is mandatory.

# Reading from a file in binary mode
k = open("azram.txt", "rb") # default mode is "rt" which is read text mode.
b = k.read()
print(b)
k.close()

# Reading characters from the file
l = open("azram.txt")
c = l.read(3)
print(c)
c = l.read(3) # The number of times we print this, the number of characters next 3 characters it will read.
print(c)
l.close()

l = open("azram.txt")
d = l.read(345)     # But if we ask for more characters present in the file, I will dump everything in the first
print("1.", d)      # iteration itself. The second iteration will go blank as we can see here.
d = l.read(345)
print("2.", d)
l.close()

# Printing line by line
m = open("azram.txt")
# a = j.read()      # If we read then the file pointer will be empty and nothing will be printed.
for line in m:      # line itself has \n so its printing new line everytime. To be clear, its not the print that's doing it.
    print(line, end="")
m.close()

# Methods to read a line
n = open("azram.txt")
print(n.readline())
print(n.readline())
print(n.readline())
n.close()

n = open("azram.txt")
print(n.readlines())   #This will create a list of the contents. You can see that the hidden \n is also revealed
n.close()       #Last line does not have new line character as could be seen here.