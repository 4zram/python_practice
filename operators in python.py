# Arithmatic Operator
print("Arithmatic Operator")
print("5 + 6 is\t", 5 + 6)
print("5 - 6 is\t", 5 - 6)
print("5 * 6 is\t", 5 * 6)
print("5 power 6 is\t", 5 ** 6) #Will give exponential value
print("15 / 6 is\t", 15 / 6)
print("15 // 6 is\t", 15 // 6) #Will give integer value
print("15 % 6 is\t", 15 % 6) #Will provide the remainder after dividing

# Assignment Operator
print("Assignment Operators")
x = 5
x += 7
print(x)
x %= 7
print(x)

# Comparison Operator
print("Comparison Operator")
i = 3; j = 7
print("3 > 7 ",i > j)
print("3 < 7 ",i < j)
print("3 <= 7 ",i <= j)
print("3 >= 7 ",i >= j)
print("3 == 7 ",i == j)
print("3 != 7 ",i != j)

# Logical Operator
a = True; b = False
print("a and a ", a and a); print("a or a ", a or a) #true true = true; as per AND, OR and other logic tables
print("a and b ", a and b); print("a or b ", a or b)
print("b and b ", b and b); print("b or b ", b or b)
print("b and a ", b and a); print("b or a ", b or a)

# Identity Operator
print(a is b)
print(a is not b) # 'is' and 'is not' are the identity operators

# Membership Operator
l = [3,6,2,32,67,321,75,56]
print("is 3 in list? ", 3 in l)
print("is 60 in list? ", 60 in l)
print("is 345 in list? ", 345 not in l)
print("is 32 in list? ", 32 not in l)

# Bitwise Operator
"""
0 - 00
1 - 01
2 - 10
3 - 11
"""
print(0 & 1)
print(0 | 1)