var1 = 5
var2 = 78
var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

# Use of 'in' and 'not in' keyword
list3 = [5,2,6,3]
print(5 in list3)
print(15 not in list3)
if 5 in list3:      # Similarly, we can use 'not in' keyword in if statement
    print("Yes, it's in the list")