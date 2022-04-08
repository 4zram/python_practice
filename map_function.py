"""
map function can iterate and process on each of the elements.
map function and reduce function helps improving performance.
"""
lis = ["3", "65", "78", "2", "0", "34", "12"]
li = [1,5,3,6,8,4,2,64,9]
# for j in range(len(lis)):     #This for loop could be converted into one line using map function.
#     lis[j] = int(lis[j])
#     lis[j] += 1
#     print(lis[j], end=", ")

a = list(map(int, lis)) #Will iterate each elements and convert it to int
print("String conversion",a)

b = list(map(lambda j:j*j,li))      #Using map for lambda function
print("squaring by lambda",b)

# Further usage of map function
def square(p):
    return p*p
def cube(q):
    return q*q*q
num = [square, cube]
for i in range(7):
    tese = list(map(lambda x:x(i), num))    #Here, i=p for num=square and i=q for num=cube
    print("Square and Cube",tese)

# *****************Reduce function***************
# n = 0
# for item in li:
#     n = n + item
# print("Sum of the elements of the list is", n)


from functools import reduce    #Reduce function is a part of functools, so we have to type it this way.

m = reduce(lambda x,y:x+y, li)  #The above for loop is reduced to one line.
print("Sum of the elements of the list is", m)