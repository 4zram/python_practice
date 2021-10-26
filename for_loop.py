lis = [['harry', 7], ['sahrish', 10], ['shifa', 8], ['azram', 3]]
#for could be used to iterate all the elements from the list.
for item in lis:
    print(item)

#we can get the iteration of each elements in the way below.
for item, num in lis:
    print(item, "the number is", num)

#we can convert the list into dictionary and get it iterated as follows
dic = dict(lis) #dict() function is used to convert that
print(dic)
for item, num in dic.items():   #we would need to use function .items() to get iterations
    print(item, "number is", num)

for item in dic:
    print(item)