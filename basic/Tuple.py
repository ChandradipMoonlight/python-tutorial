

#? Tuple

#Tuple is immutable 

# declaration

tup = (1) 
print(type(tup)); # int

# when ever ever we declare tup with single value we have to give comma after element other wise it will be consider as int
# in case of multiple element ite is optional

tup = (1,);
print(type(tup)); # tuple
tup = (1, 2, 3); # or tup = (1, 2, 3,) both are same 
print(type(tup)); # tuple

# ? Tuple methods

# 1. index(ele); returns index of first occurrence of element
tup = (1, 2, 7, 2, 4);
print(tup.index(2)); # o/p => 1

# 2. count(ele); return total occurrences of element
print(tup.count(2)); # o/p => 2