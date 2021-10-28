f = open("test1.txt", "r")
print(f.tell())     # Will tell the position of the pointer.
print(f.readline())
print(f.tell())
print(f.seek(0))    # Will take the pointer to the desired location.
print(f.readline())
print(f.seek(10))
print(f.readline())
f.close()

# use of with block
with open("test1.txt") as b:        # We won't need to close the file. With block will do that on it's own.
    print(b.readline())
    print(b.read(5))