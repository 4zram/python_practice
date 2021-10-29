# Built-in functions
a = 5
b = 8
c = sum((a , b))    # For the function to be iterable, input should be a tuple or a list
print(c)

# User function
def fun():
    """This is an introductory function"""      # This is called doc string. This is helpful to have the function description for long codes
    print("Hello you are in function")
    return 0
print(fun())    # This will print a 'NONE' which is an indication that the function didn't return anything.
print(fun.__doc__)      # This is the method to print doc string.

fun()   # This will call the fun() and run it. easiest way to call a function.

def use(i,j):
    # print("Addition of i and j is:", i+j)     # Commenting this so that it won't print twice.
    return(i+j)
v = use(5, 8)   # Inputs can also be given to the functions
print(v)    # Here, none is not printed since the function is returning some value which is 13 here.

# Lambda aka Anonymous function
minus = lambda a,b: a-b     #This is basically a one liner function
print(minus(4,2))

# Understanding Lambda by using sort function
def sor(a):
    return a[1]

a = [[34,78], [54,28], [92,10]]

a.sort(key=sor)
print(a)

a.sort(key = lambda x:x[1])     # Above example with lambda function.
print(a)