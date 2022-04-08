#Create a dictionary which takes user input and returns the meaning of that word. It is considered that
#the user will not check more than 10 words.

print("Meaning of what word are you looking for?")
var = input()
dic = {"Nincompoop":"Foolish person", "Lexicon":"This means dictionary itself",
    "Mutable":"The thing that shows some changes", "Immutable": "The thing that doesn't show any changes"}
d1 = dic.get(var)
print(d1)