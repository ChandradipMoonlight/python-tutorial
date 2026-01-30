# ========================================
# Python Lists and Tuples - Deep Concepts
# ========================================

print("===== 1. Lists =====\n")

# Lists: ordered, mutable, allow duplicates, mixed types

# Create Lists
list1 = [1, 2, 3, 4, 2, "hello", [5, 6], True]
print("List1:", list1)
# Output: List1: [1, 2, 3, 4, 2, 'hello', [5, 6], True]

# Access elements by index
print("Item at index 0:", list1[0])
print("Item at last index:", list1[-1])
print("Item at nested index list1[6][0]:", list1[6][0])
# Output:
# Item at index 0: 1
# Item at last index: True
# Item at nested index list1[6][0]: 5

# Slice
print("Slice list1[1:5]:", list1[1:5])
# Output: Slice list1[1:5]: [2, 3, 4, 2]

# Modify (Lists are mutable)
list1[2] = 100
print("Modified List1:", list1)
# Output: Modified List1: [1, 2, 100, 4, 2, 'hello', [5, 6], True]

# Add elements
list1.append("new item")    # Add at end
list1.insert(2, "inserted") # Insert at index
print("After append & insert:", list1)
# Output: After append & insert: [1, 2, 'inserted', 100, 4, 2, 'hello', [5, 6], True, 'new item']

# Extend with another iterable
list1.extend([7, 8])
print("After extend:", list1)
# Output: After extend: [1, 2, 'inserted', 100, 4, 2, 'hello', [5, 6], True, 'new item', 7, 8]

# Remove elements
list1.remove(2)       # Remove first matching value
popped = list1.pop()  # Remove last item
print("After remove & pop:", list1, "| Popped:", popped)
# Output: After remove & pop: [1, 'inserted', 100, 4, 2, 'hello', [5, 6], True, 'new item', 7] | Popped: 8

# Delete by index
del list1[3]
print("After del:", list1)
# Output: After del: [1, 'inserted', 100, 2, 'hello', [5, 6], True, 'new item', 7]

# Clear all elements
temp = [1, 2, 3]
temp.clear()
print("After clear():", temp)
# Output: After clear(): []

# List methods: index, count
a = [1, 2, 3, 2]
print("Index of 2:", a.index(2))  # returns first occurrence index
print("Count of 2:", a.count(2))
# Output:
# Index of 2: 1
# Count of 2: 2

# Sort (in-place), reverse
sort_list = [2, 4, 1, 5]
sort_list.sort()
print("Sorted list:", sort_list)
sort_list.reverse()
print("Reverse list:", sort_list)
# Output:
# Sorted list: [1, 2, 4, 5]
# Reverse list: [5, 4, 2, 1]

# Copy list
copy_list = sort_list.copy()
print("Copied list:", copy_list)
# Output: Copied list: [5, 4, 2, 1]

# List comprehension (powerful)
squares = [x ** 2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
nested = [[1, 2], [3, 4]]
flat = [y for x in nested for y in x]
print("List comprehensions:", squares, evens, flat)
# Output: List comprehensions: [0, 1, 4, 9, 16] [0, 2, 4, 6, 8] [1, 2, 3, 4]

# Nested list access
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix[1][2]:", matrix[1][2])
# Output: Matrix[1][2]: 6

# Copy vs deepcopy
import copy
orig = [[1, 2], [3, 4]]
shallow_copy = orig.copy()
deep_copy = copy.deepcopy(orig)
orig[0][0] = 99
print("Shallow copy affected:", shallow_copy)
print("Deep copy unaffected:", deep_copy)
# Output:
# Shallow copy affected: [[99, 2], [3, 4]]
# Deep copy unaffected: [[1, 2], [3, 4]]

# Membership check
print("2 in [1, 2, 3]:", 2 in [1, 2, 3])
# Output: 2 in [1, 2, 3]: True

print("\n===== 2. Tuples =====\n")

# Tuples: ordered, immutable, allow duplicates, mixed types
tuple1 = (1, 2, 3, 2, "hello", True)
print("Tuple1:", tuple1)
# Output: Tuple1: (1, 2, 3, 2, 'hello', True)

# Single-element tuple (comma required)
single = (42,)
print("Single-element tuple:", single)
# Output: Single-element tuple: (42,)

# Access by index and slice
print("Item at index 1:", tuple1[1])
print("Slice tuple1[2:5]:", tuple1[2:5])
# Output:
# Item at index 1: 2
# Slice tuple1[2:5]: (3, 2, 'hello')

# Tuples are immutable - cannot modify
try:
    tuple1[0] = 99
except TypeError as e:
    print("Tuple immutability error:", e)
# Output: Tuple immutability error: 'tuple' object does not support item assignment

# Methods: count, index
print("Count of 2 in tuple1:", tuple1.count(2))
print("Index of 'hello':", tuple1.index("hello"))
# Output:
# Count of 2 in tuple1: 2
# Index of 'hello': 4

# Iteration through tuple
for item in tuple1:
    print("Tuple item:", item)
# Outputs each item in tuple1 on a separate line

# Tuple unpacking example
a, b, c, _, _, _ = tuple1
print(f"Unpacked values: a={a}, b={b}, c={c}")
# Output: Unpacked values: a=1, b=2, c=3

# Packing and unpacking with *
first, *rest = tuple1
print("First:", first, "Rest:", rest)
# Output: First: 1 Rest: [2, 3, 2, 'hello', True]

# Nested tuples access
nested_tuple = ((1, 2), (3, 4))
print("nested_tuple[1][0]:", nested_tuple[1][0])
# Output: nested_tuple[1][0]: 3

# Mutability of mutable elements inside tuple
tuple_with_list = (1, [2, 3], 4)
tuple_with_list[1][0] = 99
print("Changed mutable inside tuple:", tuple_with_list)
# Output: Changed mutable inside tuple: (1, [99, 3], 4)

print("\n===== 3. List vs Tuple Summary =====\n")

diffs = [
    "Lists: mutable, Tuples: immutable",
    "Lists use [], Tuples use ()",
    "Tuples can be used as dictionary keys, Lists cannot",
    "Tuples have only count() and index() methods",
    "Lists have many built-in methods",
    "Tuples are faster for iteration and memory efficient",
]
for d in diffs:
    print("-", d)
# Output: listed points showing differences

print("\n===== 4. Conversion and Advanced Concepts =====\n")

# Conversion between list and tuple
tuple_from_list = tuple(list1)
list_from_tuple = list(tuple1)
print("Tuple from list:", tuple_from_list)
print("List from tuple:", list_from_tuple)
# Outputs converted collections

# zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print("Zipped list:", zipped)
# Output: Zipped list: [(1, 'a'), (2, 'b'), (3, 'c')]

# max, min, sum example
nums = [5, 8, 2, 9]
print("Max:", max(nums), "Min:", min(nums), "Sum:", sum(nums))
# Output: Max: 9 Min: 2 Sum: 24

# all() and any()
bools = [True, False, True]
print("all(bools):", all(bools), "any(bools):", any(bools))
# Output: all(bools): False any(bools): True

# enumerate()
for index, val in enumerate(nums):
    print(f"Index {index}: Value {val}")
# Outputs index and value for each item

# Mutable Default Arg Demo (interview tricky)
def mutable_default_test(arg=[]):
    arg.append(1)
    return arg

print("Mutable default call 1:", mutable_default_test())
print("Mutable default call 2:", mutable_default_test())
# Output:
# Mutable default call 1: [1]
# Mutable default call 2: [1, 1]

# Tuple as dictionary key
my_dict = {(1, 2): "tuple key", "string": "value"}
print("Dict value for tuple key:", my_dict[(1, 2)])
# Output: Dict value for tuple key: tuple key

print("\n=== End of file ===")
