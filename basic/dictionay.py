# ===================================
# Python Dictionaries - Concepts and Examples
# Reference: Shradha Khapra YouTube + Official Docs
# ===================================

print("===== 1. What is a Dictionary? =====")
# A dictionary stores key-value pairs.
# Keys are unique, immutable types (strings, numbers, tuples),
# Values can be any data type.

# Creating a dictionary with mixed value types
my_dict = {
    "name": "Rahul",
    "age": 25,
    "is_student": True,
    "marks": [85, 90, 92]
}
print("Dictionary:", my_dict)
# Output: Dictionary: {'name': 'Rahul', 'age': 25, 'is_student': True, 'marks': [85, 90, 92]}

print("\n===== 2. Accessing Values =====")
print("Name:", my_dict["name"])
print("Marks:", my_dict["marks"])
# Output:
# Name: Rahul
# Marks: [85, 90, 92]

print("\n===== 3. Modifying Values =====")
my_dict["age"] = 26  # Update existing key
my_dict["city"] = "Mumbai"  # Add new key-value pair
print("Updated dictionary:", my_dict)
# Output:
# Updated dictionary: {'name': 'Rahul', 'age': 26, 'is_student': True, 'marks': [85, 90, 92], 'city': 'Mumbai'}

print("\n===== 4. Removing Items =====")
my_dict.pop("is_student")  # Removes 'is_student' key
print("After pop('is_student'):", my_dict)

removed_value = my_dict.popitem()  # Removes last inserted item (as of Python 3.7+)
print("After popitem():", my_dict)
print("Removed item:", removed_value)
# Output:
# After pop('is_student'): {'name': 'Rahul', 'age': 26, 'marks': [85, 90, 92], 'city': 'Mumbai'}
# After popitem(): {'name': 'Rahul', 'age': 26, 'marks': [85, 90, 92]}
# Removed item: ('city', 'Mumbai')

print("\n===== 5. Keys, Values, and Items =====")
print("Dictionary keys:", my_dict.keys())
print("Dictionary values:", my_dict.values())
print("Dictionary items:", my_dict.items())
# Output:
# Dictionary keys: dict_keys(['name', 'age', 'marks'])
# Dictionary values: dict_values(['Rahul', 26, [85, 90, 92]])
# Dictionary items: dict_items([('name', 'Rahul'), ('age', 26), ('marks', [85, 90, 92])])

print("\n===== 6. Dictionary Methods =====")

# Copying dictionary
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# Clearing dictionary
temp_dict = copied_dict.copy()
temp_dict.clear()
print("Cleared dictionary:", temp_dict)

# Check membership for keys
print("'name' in dictionary?", 'name' in my_dict)
print("'Mumbai' in dictionary?", 'Mumbai' in my_dict)  # False, membership applies to keys only

print("\n===== 7. Nested Dictionaries =====")
nested_dict = {
    "student1": {
        "name": "Ankit",
        "marks": {"math": 90, "physics": 85}
    },
    "student2": {
        "name": "Sneha",
        "marks": {"math": 92, "physics": 88}
    }
}
print("Nested dictionary:", nested_dict)

print("Student1 Math marks:", nested_dict["student1"]["marks"]["math"])
# Output:
# Nested dictionary: {'student1': {'name': 'Ankit', 'marks': {'math': 90, 'physics': 85}}, 'student2': {'name': 'Sneha', 'marks': {'math': 92, 'physics': 88}}}
# Student1 Math marks: 90

print("\n===== 8. Using get() method =====")
print("Get 'name':", my_dict.get("name"))
print("Get 'city' (non-existing):", my_dict.get("city"))  # Returns None instead of error
print("Get 'city' with default:", my_dict.get("city", "Not specified"))
# Output:
# Get 'name': Rahul
# Get 'city' (non-existing): None
# Get 'city' with default: Not specified

print("\n===== 9. Update Method =====")
extra_info = {"city": "Pune", "age": 27}
my_dict.update(extra_info)
print("After update:", my_dict)
# Output:
# After update: {'name': 'Rahul', 'age': 27, 'marks': [85, 90, 92], 'city': 'Pune'}

print("\n===== 10. Iterating over Dictionary =====")
for key, value in my_dict.items():
    print(f"{key} => {value}")

# Example output:
# name => Rahul
# age => 27
# marks => [85, 90, 92]
# city => Pune

print("\n===== 11. Important Notes =====")
print("- Dictionary keys must be immutable (str, int, tuple, etc.)")
print("- Values can be any type including lists, dicts, etc.")
print("- Dictionaries are mutable (can modify keys and values)")
print("- Python 3.7+ maintains insertion order in dictionaries")

# ================================
# End of Dictionary Concepts & Examples
# ================================
