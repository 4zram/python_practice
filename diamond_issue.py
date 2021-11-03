"""
Here, suppose class B & C is inherited from A and class D is the child of B and C both, then this creates a diamond issue(confusion)
Most of the languages struggle to solve this diamond issue in case of multiple inheritance. Hence, it's recommended to avoid multiple inheritance.
"""
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    # def met(self):
    #     print("This is a method from class B")
    pass        # used for an empty class, loops or anything.

class C(A):
    # def met(self):
    #     print("This is a method from class C")
    pass

class D(C, B):
    # def met(self):
    #     print("This is a method from class D")
    pass


a = A()
b = B()
c = C()
d = D()

d.met()