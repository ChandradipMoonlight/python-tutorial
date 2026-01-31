
# String and its methods
# String is immutable in python once object is created we can not change its content it create new object

#? 1. len(<string>) => return length of the string

name = "Pooja";
print("Length of string 'Pooja' : ",len(name)); # 5

#? 2. index in string
print("character at position 0 = ", name[0]); # o/p => n

#? 3. slice 
#  str[startIndexIncluding : endIndexExcluding]
#  str[startIndexIncluding : endIndexExcluding : numberOfStepsToBeSkip] numberOfStepsToBeSkip is optional by default it is 1
stringSlice = name[2 : len(name)]; # o/p => oja or name[2:] or name[2: -1] are same
print("String between 2 to end : ", stringSlice);

stringSlice = name[0 : -1: 2]; # -1 mean last index of string o/p=> Po or name[::2] or name[0::2] are same
print("String between 0 to end with step 1", stringSlice) # o/p => Pj or name[0::2] are same

# name[ : 3] is same as name[0 : 3]
# name[2 : ] is same as name[2 : len(name)]
# name[ : 3] is same as name[0 : 3]

#? 4. str.endsWith("subString");
# return true if string end with subString else return false

str = "python tutorial";
print(str.endswith("ial")); # True
print(str.endswith("Tuto")); # False

#? 5) str.capitalize();
# Capitalize first char of string
print(str.capitalize()); # Python tutorial

#? 6) str.replace( old, new ) 
# replaces all occurrences of old subString with new subString
# Return a copy with all occurrences of substring old replaced by new.

print(str.replace("a", "A")); # python tutoriAl
print(str.replace("t", "T")); # pyThon TuTorial
print(str.replace("thon", "")); # py tutorial

#? 7) str.find("subString");
# return first index of fist occurrence else -1
print(str.find("ram")); # -1
print(str.find("th")); # 2

#? 8) str.count(“am“) 
#counts the occurrence of substr in string

print(str.count("t")); # 3


# Palindrome Checker
codingQue = '''1. Input a string and check if it reads the same backward.
Example: "madam" → palindrome

2. Count Vowels and Consonants
Input a word and print number of vowels and consonants.'''


print("5. Palindrome Checker")

# word = input("please enter any word : ")
word = "madam"

reversedWord = word[::-1]
if word==reversedWord:
    print("Palindrome")
else:
    print("Not Palindrome")

