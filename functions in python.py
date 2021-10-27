# Built-in functions
a = 5
b = 8
c = sum((a , b))    # For the function to be iterable, input should be a tuple or a list
print(c)

# User function
def fun():
    print("Hello you are in function")
print(fun())    # This will print a 'NONE' which is an indication that the function didn't return anything.

fun()   # This call the fun() and run it. easiest way to call a function.

def use(i,j):
    print("Addition of i and j is:", i+j)
    return(i+j)
v = use(5, 8)   # Inputs can also be given to the functions
print(v)    # Here, none is not printed since the function is returning some value which is 13 here.