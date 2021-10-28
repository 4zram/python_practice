"""
Recursion means calling a function from within a function. This calling should break to avoid recursion error.
"""

# def hellow():
#     hellow()      # There is no break in calling, so, this will throw recursion error.
#     print("This is recursion")
# hellow()

# Factorial by iterative method
num = int(input("Enter you number:"))
def fac_iterative(n):
    """Fartorial using iterative method"""
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
print("Factorial by iterative method", fac_iterative(num))

# Factorial by recursive method
def fac_recursive(n):
    """Factorial using recursive method"""
    if n == 1:
        return 1
    else:
        return n * fac_recursive(n-1)
print("Factorial by recursive method", fac_recursive(num))

"""
for n = 5
5 * fac_recursive(4)
5 * 4 * fac_recursive(3)
5 * 4 * 3 * fac_recursive(2)
5 * 4 * 3 * 2 * fac_recursive(1)
"""

# Fibonachi series for nth number by iteration method
def fib_it(n):
    a = 0
    b = 1
    count = 0
    if n <= 0:
        print("Enter a positive number greater than 0")
    else:
        while count<n:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1
num = int(input("Enter nth number"))
print(fib_it(num))

# Fibonachi series of nth number by recursive method
def fib_re(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_re(n-1) + fib_re(n-2)
num = int(input("Enter nth number"))
print(fib_re(num))