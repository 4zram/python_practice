# Creating a file
f = open("test.txt", "w")
f.write("Azram, you are awesome, perfect, deserving and everything that you think you arn't.\n"
        "This file is created by running 'file write' file")
f.close()

# Appending a file
f = open("test1.txt", "a")
f.write("Azram, you are awesome, perfect, deserving and everything that you think you arn't.\n"
        "This file is created by running 'file write' file\n")
f.close()

# Handling reading and writing both. 'r+' has higher priority than all others.
f = open("test2.txt", "r+")          # 'r+' will give the ability to read and write to a file at the same time.
print(f.read())
f.write("\nThis text is written by 'r+' from 'file write' file")
f.close()

# To read the number of characters of a file
f = open("test.txt", "w")
a = f.write("Azram, you are awesome, perfect, deserving and everything that you think you arn't.\n"
        "This file is created by running 'file write' file")
print(a)
f.close()