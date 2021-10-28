f = open("test1.txt", "r")
print(f.tell())     # Will tell the position of the pointer.
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.seek(0))    # Will take the pointer to the desired location.
print(f.readline())
print(f.seek(10))
print(f.readline())