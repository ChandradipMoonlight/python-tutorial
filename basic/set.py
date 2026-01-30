# ===================================
# Python Sets - Concepts and Examples
# Reference: Shradha Khapra YouTube + Official Docs
# ===================================

print("===== 1. What is a Set? =====")
# A set is an unordered collection of unique elements.
# Sets do not allow duplicates.

# Creating a set
my_set = {1, 2, 3, 4, 4, 3}
print("Set with duplicates removed:", my_set)
# Output: Set with duplicates removed: {1, 2, 3, 4}

# Creating an empty set ({} creates empty dict!)
empty_set = set()
print("Empty set:", empty_set)
# Output: Empty set: set()

print("\n===== 2. Set Properties =====")
# Sets are unordered: no indexing or slicing
# Sets can store heterogeneous elements
hetero_set = {1, "hello", 3.14, True}
print("Heterogeneous set:", hetero_set)
# Output example: Heterogeneous set: {True, 1, 3.14, 'hello'}

print("\n===== 3. Adding and Removing Elements =====")
s = {1, 2, 3}
print("Original set:", s)

# Add element (adds silently if element exists)
s.add(4)
print("After add(4):", s)

# Remove element (throws error if element not present)
s.remove(2)
print("After remove(2):", s)

# Discard element (does not throw error if element not present)
s.discard(10) 
print("After discard(10) - no effect:", s)

# Pop element (removes and returns arbitrary element)
popped = s.pop()
print("After pop():", s, "| Popped element:", popped)

print("\n===== 4. Set Operations =====")
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))  # or set1 | set2

# Intersection
print("Intersection:", set1.intersection(set2))  # or set1 & set2

# Difference
print("Difference (set1 - set2):", set1.difference(set2))  # or set1 - set2

# Symmetric difference (elements in either set, but not both)
print("Symmetric difference:", set1.symmetric_difference(set2))  # or set1 ^ set2

print("\n===== 5. Set Membership & Length =====")
print("Is 2 in set1?", 2 in set1)  # True
print("Is 10 in set1?", 10 in set1)  # False
print("Length of set1:", len(set1))

print("\n===== 6. Set Methods Summary =====")
print("Methods: add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), isdisjoint(), copy()")

# Check subset, superset and disjoint
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print("A is subset of B?", A.issubset(B))
print("B is superset of A?", B.issuperset(A))
print("A and B are disjoint?", A.isdisjoint(B))

print("\n===== 7. Important notes =====")
print("- No duplicates allowed")
print("- Sets are unordered, so no indexing")
print("- Sets can be used for fast membership tests")
print("- Elements must be immutable (e.g. no lists inside sets)")

print("\n===== 8. Set Example: Removing duplicates from a list =====")
lst = [1, 2, 3, 2, 4, 1, 5]
unique_elements = set(lst)
print("List:", lst)
print("Unique elements as set:", unique_elements)
print("Unique elements as list:", list(unique_elements))

# ===================================
# End of Set Concepts and Examples
# ===================================
