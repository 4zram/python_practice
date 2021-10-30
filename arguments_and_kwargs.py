"""
Arguments here are used to make the program scalable. By following this, we can alter the arguments that
was supposed to be passed through function.
The format for this is func(normal, *args, **kwarks)
if you flip any of those positions, it will throw error
"""

def func(a, *args):    #args will always be tupple here, does not matter if you give list or tupple.
    print(a)
    for item in args:
        print(item)

def funct(a, *list, **kwargs):  #It's not mandatory to name it args and kwargs. You can use any name.
    print(a)
    for item in list:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

l = ["Azram", "Shifa", "Sahrish"]
a = "Rajesh"    # We can pass a normal argument as we used to do.
d = {"Azram":"Engineer", "Shifa":"Student", "Sahrish":"Struggling student"}

print("Scope of this program is within ", __name__)
# Above print will show the scope of the program, if it is in main or being imported somewhere.
if __name__ == '__main__':
    func(a, *l)
    funct(a, *l, **d)