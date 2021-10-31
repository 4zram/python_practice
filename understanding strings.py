mystr = "Hey man! How you doing?"
print(mystr) #prints the string

print(len(mystr)) #will print the length of the string

print(mystr [10:20]) #will slice the part of the string as per desire.

print(mystr [:5]) #It will take the first as 0 itself

print(mystr [0:]) #it will print the whole string

print(mystr [0:22])
#remember that the last one is always excluding. This won't print full string as 22 is exluding

print(mystr [0:10:2])
#Extended slicing. Here, out of the output string every second letter will be skipped

print(mystr [::]) #here, 0; string length; 1 is considered on it's own

print(mystr [-6:-2]) #will count the 6th and 3rd from the end

print(mystr [17:21]) #exactly same as above just not in negation

print(mystr [::-1]) #will invert the whole string

print(mystr.isalnum())
"""will check for alpha numeric characters and print boolean True/False if couldn't find any.
Here, in this case, space does not come in alpha or numeric so it will present False"""

print(mystr.isalpha()) #Checks for alpha & False due to same reasons as space is not alpha

print(mystr.endswith("?")) #to verify the ending of the string

print(mystr.count("H")) #will count the number of H in the string

print(mystr.capitalize()) #will capitalize the first letter

print(mystr.find("you")) #will find and print the location of the input

print(mystr.lower()) #will print whole string in lowercase. Similarly upper() would do the opposite.

print(mystr.replace("you", "we")) #will replace you with we