# Dictionary is just Key-value pair. Dictionary is case sensitive.
# Keys in a tuple or list or dictionary should be immutable
d = {}
l = []
t = ()
print(type(d))
print(type(l))
print(type(t))

#Printing key-values of a dictionary
di = {"Deepak": "Friend", "Shourya": "Athelete", "Hardy": "Bhaiya"}
print(di)
print(di["Deepak"])
# print(di["hardy"])  # H should be in caps.
print(di.get("Hardy")) #to get key-value using functions which is more preferred

#We could put a dictionary inside a dictionary itself
dy = {"Parents": "Children", "nickname": {"sahrish": "mota bheem", "shifa": "shipfu panda"}}
print(dy["Parents"])
print(dy["nickname"])
print(dy["nickname"]["sahrish"])

#adding a key-value to the dic
dy["Sister"] = "Sahrish"
print(dy)

#another method to add which is by the help of function and more preferred one.
di.update({"Shadab":"Family Friend"})
print(di)

#deleting a key-value from the dic
del dy["Parents"]
print(dy)

#copy creating another dict
gem = di.copy()
del di["Shourya"]
print(gem)
print(di)

#printing items and keys
print(dy.keys())
print(dy.items())