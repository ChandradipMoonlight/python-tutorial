
## List is build in data type that stores group of values
## it can store element of different datatypes 
data = ["Pune", 76, True, 45.9];
print("Heterogeneous type list, data :: ", data);
## list is mutable



marks = [74, 87, 78, 95, 91];
print("Marks :: ", marks);
marks.append(65); # append element at the end of list and return None
print("after appending 65, Marks :: ", marks);

print("length of Marks List = ", len(marks)); # 6

marks.sort(); # sort in ascending order
print("sorted in ascending order :: ", marks);
marks.sort(reverse=True);
print("sorted in reverse order that is descending order :: ", marks)

productPrice = [99.99, 56, 678, 451];
productPrice.reverse();
print("Reversed array of productPrice :: ", productPrice);
productPrice.sort();
print("sorted productPrice in ascending order :: ", productPrice);

# ! list.insert(index, ele);
# insert given element at given index;

productPrice.insert(1, 100);
print("productPrices after insertion operation :: ", productPrice);

list = [2, 1, 3, 1]


list.remove(1) #removes first occurrence of element. [2, 3, 1]
print(list); # [2, 3, 1]

list.pop( 2 ) #removes element at given idx [2, 3]
print(list);


import copy

print("=== Shallow Copy Example ===")

# Original nested list
original = [[1, 2], [3, 4]]

# Create shallow copy
shallow_copy = copy.copy(original)

# Modify nested element in shallow copy
shallow_copy[0][0] = 99

print("Original after shallow copy modification:", original)
print("Shallow copy:", shallow_copy)

# Output:
# Original after shallow copy modification: [[99, 2], [3, 4]]
# Shallow copy: [[99, 2], [3, 4]]

print("\n=== Deep Copy Example ===")

# Reset original list
original = [[1, 2], [3, 4]]

# Create deep copy
deep_copy = copy.deepcopy(original)

# Modify nested element in deep copy
deep_copy[0][0] = 100

print("Original after deep copy modification:", original)
print("Deep copy:", deep_copy)

# Output:
# Original after deep copy modification: [[1, 2], [3, 4]]
# Deep copy: [[100, 2], [3, 4]]




