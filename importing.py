"""
you can import any of the file and it will work just fine and same.

Sys.path will show the path where the program will look for the modules and then import it from there.
It will check for the modules in the paths output in an ascending manner.

if __name__=='__main__' is only used so that instead of running the whole program, it only runs whatever is
imported and called for. The absence of that will give the output of whole program to the imported program.
"""
import sys
for item in sys.path:
    print(item)
import arguments_and_kwargs
l = ["Suresh", "Jignesh", "Haritesh"]
a = "Ramesh"
dic = {"Rajesh":"Gardner", "Hari":"Musicion", "Himesh":"Struggler"}
print(arguments_and_kwargs.func(a, *l))
print(arguments_and_kwargs.funct(a, *l, **dic))