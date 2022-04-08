var1 = "hello"
var2 = 4
var3 = 54.8
var4 = "azram"
var5 = "45"
var6 = "73"

print(type(var1)) #to check the type of the variable. Similarly, could be done for all of them

print(var3 + var2) #normal additions of float and int

print(var1 + var4) #strings when added will be concatinated

print(var5 + var6) #strings when added will be concatinated

print(int(var5) + int(var6)) #converting string into int which is called type casting
#str() ; int() ; float() could be used as per requirement for conversion

#print(var1 + var2) #string and int/float addition is not possible

print(10 * "hello\n") #can provide repetetive output of a single input.

print(10 * str(int(var5) + int(var6))) #way to print multiple times. Here, this was again converted to string.

print("Enter your number")
var10 = input() #this takes input as strings
print("adding 10 to your number becomes", int(var10) + 10) #had to do the type casting for such additions.