print("Hello World");

# data types = there are five type of data type in python

# 1. Integer,
# 2. Float,
# 3. Boolean,
# 4. String,
# 5. None


name = "Ram";
name1 = 'Ram';
name2 = '''Ram''' # multi line string declaration
name3 = """My name is Ram.
I am a student of computer science and engineering.
I am from India.
I am 20 years old.
I am a good student.
"""
# used for multi line string declaration

# above all are valid declaration of string

print(type(name)); 
print(type(name1));
print(type(name2));

# o/p above all three print are same => <class 'str'> 

prince = 12.34; # float
age = 28; # int
check = True; # boolean value in python are = True/False
a = None; # NonType

# ? arithmetic operation

a = 12;
b = 2;

print(a+b); # sum = 14;
print(a*b); # multi = 24;
print(a/b); # div = 6.0;
print(a%b); # reminder = 0;
print(a**b); # power (a^b) = 144;

# ! Expression execution
# string and numeric value can operate together only with *

a, b = 2, 3;
text = "@";
print(a*text*b); # o/p => @@@@@@

a = "7";
print(a+text); # p/p => 7@

print(a+text*b); # o/p => 7@@@

print((a+text)*b); # o/p => 7@7@7@

# ! input in python

# String input

name = input("name : ");
print("string input "+name);

# int input
# input always return string so we have to typecast it to int
age = int(input("age : "));
print("int input = "+str(age));

# float input
price = float(input("price : "));
print("Float input :: "+str(price));

