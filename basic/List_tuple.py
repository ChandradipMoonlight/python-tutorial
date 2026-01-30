# =======================
# Python Lists and Tuples
# =======================

print("======== 1. List Concept and Examples ========")

# 1. What is a List?
# - Lists are ordered, mutable collections that can store mixed data types.
# - Lists are defined with square brackets: []
# - Syntax: my_list = [element1, element2, ...]

# Example 1: Creating and printing a list
my_list = [10, 20, 30, "Python", 25.5]
print("List:", my_list) # o/p => List: [10, 20, 30, 'Python', 25.5]

# Example 2: Accessing elements (zero-based indexing)
print("First element:", my_list[0]) # o/p => First element: 10
print("Last element:", my_list[-1])  # Negative index for last item, o/p => 25.5

# Example 3: Slicing a list
print("Slice [1:4]:", my_list[1:4]) # o/p => Slice [1:4]: [20, 30, "Python"]

# Example 4: Modifying list elements (lists are mutable)
my_list[1] = 99
print("After changing 2nd element:", my_list) # o/p => After changing 2nd element: [10, 99, 30, "Python", 25.5]

# Example 5: List methods
my_list.append("New")          # Add to end
print("After append:", my_list) # o/p => 
my_list.insert(2, "Insert")    # Insert at index 2
print("After insert:", my_list)
my_list.remove("Python")       # Remove by value
print("After remove 'Python':", my_list)
popped_item = my_list.pop()    # Remove last item
print("After pop:", my_list, ", Popped:", popped_item)
print("List length:", len(my_list))  # Length of list

# Example 6: Looping through a list
for item in my_list:
    print("Item:", item)

print("\n======== 2. Tuple Concept and Examples ========\n")

# 2. What is a Tuple?
# - Tuples are ordered, immutable collections that can store mixed data types.
# - Tuples are defined with parentheses: ()
# - Syntax: my_tuple = (element1, element2, ...)

# Example 7: Creating and printing a tuple
my_tuple = (10, 20, 30, "Python", 25.5)
print("Tuple:", my_tuple)

# Example 8: Accessing elements (zero-based indexing)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Example 9: Slicing a tuple
print("Slice [1:4]:", my_tuple[1:4])

# Example 10: Tuple is immutable (cannot change elements)
try:
    my_tuple[1] = 99  # Will raise an error
except TypeError as e:
    print("Cannot modify a tuple:", e)

print("\n======== 3. Tuple Methods and Iteration ========\n")

# Example 11: Tuple methods (only count and index)
print("Count of 30:", my_tuple.count(30))
print("Index of 'Python':", my_tuple.index("Python"))

# Example 12: Looping through a tuple
for item in my_tuple:
    print("Tuple item:", item)

print("\n======== 4. Differences Summary ========\n")
print("List: Mutable, many methods, uses []")
print("Tuple: Immutable, limited methods, uses ()")

# Bonus: Conversion between list and tuple
converted_tuple = tuple(my_list)
print("List to tuple:", converted_tuple)
converted_list = list(my_tuple)
print("Tuple to list:", converted_list)
