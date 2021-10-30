lis = ["3", "65", "78", "2", "0", "34", "12"]
for item in lis:
    item = int(item)
    item += 1
    print(item, end=", ")

for j in range(len(lis)):
    lis[j] = int(lis[j])
    lis[j] += 1
    print(lis[j], end=", ")