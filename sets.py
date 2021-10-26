#Sets retains unique value only
s = set()
l = [2,5,6,2,6,1,5]
var = set(l)
print(var)

#adding up some numbers in set inside the list
b = set([3,7,9])
b.add(4)
print(b)
s1 = b.union([5,8,2]) #union function unites both of the sets. Similarly, we can do intersection, disjoint and further
print(b,s1)