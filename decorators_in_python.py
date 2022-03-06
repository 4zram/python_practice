
# A function can be returned by a function
def call(fun):
    if fun == 0:
        return print
    if fun == 1:
        return int

a = call(0)
b = call(1)
print(a, b)

# A function can be passed as an argument as well
def dif(fic):
    fic("Function Executed")

dif(print)

# Decorators

# def dec1(func1):
#     def nowexec():
#         print("Executing Now")
#         func1()
#         print("Func1 executed")
#     return nowexec()
#
# def who_is_harry():
#     print("Who is Harry")
#
# who_is_harry = dec1(who_is_harry)
# who_is_harry()

# This decoration can be done by another method

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Func1 executed")
    return nowexec
@dec1
def who_is_harry():
    print("Who is Harry")

# who_is_harry = dec1(who_is_harry)
who_is_harry()