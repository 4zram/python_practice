#all the functions when applied, will change the original list
grocery = ["bhindi", "tamatar", "onions", "potato", "rice", 34] #number will be treated as int only

print(grocery[3]) #will print 3rd item from the grocery list

numbers = [2, 10, 59, 4, 8]
print(numbers.sort()) #This won't sort print directly. To do that we must run the numbers.sort() alone
numbers.sort() #similarly we can do numbers.reverse(). This will alter the original list.
print(numbers)

#slicing works very similar to string here as well

print(numbers[::-2]) #its recomended to not use negative as the output won't be expected and troublesome
print(numbers[1:5:-2]) #just by mentioning start and end, the output has seen the trouble

numbers.append(4) #this will append the integer at the end of the list.
print(numbers)

numbers.insert(2, 34) #to insert 34 at the second index. So, 2 here is place and 34 is the int you want to add
print(numbers)

numbers.remove(59) #will remove 59 from the list
print(numbers)

numbers.pop() #will remove the last value from the list
print(numbers)

numbers[0] = 32 #this will change the 0th value of the list to the assigned value.
print(numbers)

"""What if you don't want your list to be changed like done above. For that we use Tuple.
List is mutable and tuple is immutable. Mutable meanse can change while Immutable meanse can not change"""

tp = (1,4,6,2,6) #Tuple has parenthesis while list has square brackets.
print(tp)

top = (5) #single int won't create tuple. we would need to add comma to make it a tuple
print(top)

tup = (4,) #now this is a tuple
print(tup)

#to swap numbers, its very easy here.
a = 5
b = 7
a,b = b, a
print("The value of a is", a, "The value of b is", b)
"""Traditionally, we would have to follow the method below
a = temp
a = b
b = temp
but here, these 3 steps are combined in 1 single step"""