a = int(input("Choose your number:\n"))
b = int(input("Chose between 1 or 0\n"))
c = bool(b)
if c==True:
    for i in range(0,a):
        for j in range(0,i+1):
            print("*",end="")
        print()
elif c==False:
    for i in range(0,a):
        for j in range(0,a-i):
            print("*",end="")
        print()