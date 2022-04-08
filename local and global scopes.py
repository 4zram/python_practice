"""
Scope is the reachability of any variable, value etc. Global variable has read only permission unless
global keyword is used.
"""

l = 19  # Global variable. Has a scope throughout the program
def functions(n):
    l = 15  # Local variable. Has a scope only within the function.
    m = 13  # Local variable. Has a scope only within the function.
    print(n, "You are in the function now.")
    print(l,m)
functions("Calling Function!")
print(l)
# print(m)    # This would throw error since m's scop is within the function only.

# In order to give write permission to a function to change global variable, we would use 'global' keyword
a = 13
def func(n):
    global a
    a = a + 1   # This would throw error if the above line was commented out
    print(n, "You are in the function now.")
    print(a)
func("Calling function!")

# global permissions in case of nested function
b = 13
def harry():
    b = 17
    def rohan():
        global b    # This would access the global variable, not to be confused with harry() variable.
        b = 58
    print("Before calling rohan()", b)
    rohan()
    print("After calling rohan()", b)
harry()
print("Total out of func call", b)