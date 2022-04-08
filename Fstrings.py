# Method 1. Readibility is tough for bigger strings so, this method was dropped.
b = "Azram and he is a good boi." \
    "Hope you got the idea"
a = "This is %s" %b
print(a)

# Method 2. Readibility is tough for bigger strings so, this method was dropped.
this = "Azram"
that = 3
out = "This is %s %s"%(this, that)
print(out)

inp = "This is {} {}"
out1 = inp.format(this,that)
print(out1)

inp1 = "This is {1} {0}" # Here, 'that' will be give first priority and 'this' will be given second priority
out2 = inp1.format(this,that)
print(out2)

# To have better redability, F strings were introduced. F in f string means fast itself
import math
output = f"This is {this} {that} {math.cos(45)}" # we can use functions here as well
print(output)