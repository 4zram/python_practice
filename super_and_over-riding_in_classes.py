"""
Class B's init has completely over-ridden the Class A's init and everything from class B will be printed unless
super().__init__() isn't being used.
So super calls for the functions from class A and b.var1 value is set to "This is init from class A" but further in the
code, the value changes to "This is init from class B but a copy from class A" which gets printed.
If super was written at the end of the constructor, it would have executed B's constructor first and then A's constructor.
"""
class A:
    var1 = "This is from class A"

    def __init__(self):
        self.var1 = "This is init from class A"
        self.var2 = "This is init from class A but a copy from class B"

class B(A):
    var1 = "This is from class B"

    def __init__(self):
        super().__init__()      # To print class A attributes, we need this, but class B's attributes will be printed unless it's in the last line.
        self.var2 = "This is init from class B"
        self.var1 = "This is init from class B but a copy from class A"

a = A()
b = B()

print(a.var1, b.var1, b.var2)   # Here, it's clear that class attributes are not being printed. To do that we need super().__init__
print(b.var1)
print(a.var2)