# ===================================
# Python Functions & Recursion - Comprehensive Concepts and Examples
# Source: Python Official Documentation & Tutorial
# ===================================

print("===== 1. Basic Function Definition =====")
# A function is a block of reusable code that performs a specific task
# Functions are defined using the 'def' keyword

def greet():
    """Simple function without parameters"""
    print("Hello, Welcome to Python Functions!")

greet()  # Calling the function
# Output: Hello, Welcome to Python Functions!

print("\n===== 2. Functions with Parameters =====")
# Functions can accept parameters (inputs)

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet_person("Rahul")
# Output: Hello, Rahul!

def add_numbers(a, b):
    """Function with multiple parameters"""
    result = a + b
    print(f"Sum of {a} and {b} is {result}")

add_numbers(5, 3)
# Output: Sum of 5 and 3 is 8

print("\n===== 3. Return Statement =====")
# Functions can return values using 'return' keyword

def multiply(x, y):
    """Function that returns a value"""
    return x * y

result = multiply(4, 7)
print(f"Multiplication result: {result}")
# Output: Multiplication result: 28

def check_even_odd(num):
    """Function returning string based on condition"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"10 is {check_even_odd(10)}")
print(f"7 is {check_even_odd(7)}")
# Output:
# 10 is Even
# 7 is Odd

# Function can return multiple values (as a tuple)
def get_name_age():
    """Function returning multiple values"""
    return "Ankit", 25

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")
# Output: Name: Ankit, Age: 25

print("\n===== 4. Default Parameters =====")
# Parameters can have default values

def greet_with_default(name, greeting="Hello"):
    """Function with default parameter"""
    print(f"{greeting}, {name}!")

greet_with_default("Sneha")  # Uses default greeting
# Output: Hello, Sneha!

greet_with_default("Sneha", "Hi")  # Overrides default
# Output: Hi, Sneha!

def calculate_power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

print(f"5^2 = {calculate_power(5)}")
print(f"5^3 = {calculate_power(5, 3)}")
# Output:
# 5^2 = 25
# 5^3 = 125

print("\n===== 5. Keyword Arguments =====")
# Arguments can be passed by name (order doesn't matter)

def student_info(name, age, city):
    """Function demonstrating keyword arguments"""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments (order matters)
student_info("Rahul", 25, "Mumbai")
# Output: Name: Rahul, Age: 25, City: Mumbai

# Keyword arguments (order doesn't matter)
student_info(city="Pune", name="Priya", age=23)
# Output: Name: Priya, Age: 23, City: Pune

# Mix of positional and keyword arguments
student_info("Amit", city="Delhi", age=27)
# Output: Name: Amit, Age: 27, City: Delhi

print("\n===== 6. *args (Variable Length Arguments) =====")
# *args allows function to accept any number of positional arguments

def sum_all(*args):
    """Function accepting variable number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
# Output:
# Sum of 1,2,3: 6
# Sum of 1,2,3,4,5: 15

def print_info(*args):
    """Print all arguments"""
    for arg in args:
        print(arg, end=" ")
    print()

print_info("Python", "is", "awesome")
# Output: Python is awesome

print("\n===== 7. **kwargs (Keyword Variable Arguments) =====")
# **kwargs allows function to accept any number of keyword arguments

def print_student_details(**kwargs):
    """Function accepting variable keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_details(name="Rahul", age=25, city="Mumbai", grade="A")
# Output:
# name: Rahul
# age: 25
# city: Mumbai
# grade: A

def create_profile(**kwargs):
    """Create user profile from keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = create_profile(first_name="Ankit", last_name="Sharma", email="ankit@example.com")
print(f"User profile: {user}")
# Output: User profile: {'first_name': 'Ankit', 'last_name': 'Sharma', 'email': 'ankit@example.com'}

print("\n===== 8. Combining *args and **kwargs =====")
# Functions can use both *args and **kwargs together

def flexible_function(*args, **kwargs):
    """Function with both *args and **kwargs"""
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

flexible_function(1, 2, 3, name="Rahul", age=25)
# Output:
# Positional arguments (*args): (1, 2, 3)
# Keyword arguments (**kwargs): {'name': 'Rahul', 'age': 25}

print("\n===== 9. Lambda Functions (Anonymous Functions) =====")
# Lambda functions are small anonymous functions defined with 'lambda' keyword

# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
# Output: Square of 5: 25

add = lambda a, b: a + b
print(f"Sum of 3 and 4: {add(3, 4)}")
# Output: Sum of 3 and 4: 7

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(f"Product of 2, 3, 4: {multiply(2, 3, 4)}")
# Output: Product of 2, 3, 4: 24

# Lambda functions are often used with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# map() is a built-in function that applies a function to each item in an iterable and returns a new list
print(f"Squared numbers: {squared}")
# Output: Squared numbers: [1, 4, 9, 16, 25]

# filter() is a built-in function that filters items from an iterable based on a condition and returns a new list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
# Output: Even numbers: [2, 4]

print("\n===== 10. Recursion =====")
# Recursion: A function calling itself

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
# Output: Factorial of 5: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

def fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(7): {fibonacci(7)}")
# Output: Fibonacci(7): 13
# Explanation: 0, 1, 1, 2, 3, 5, 8, 13, ...

def power_recursive(base, exponent):
    """Calculate power using recursion"""
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power_recursive(base, exponent - 1)

print(f"2^5 = {power_recursive(2, 5)}")
# Output: 2^5 = 32

def sum_digits(n):
    """Sum of digits using recursion"""
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

print(f"Sum of digits in 1234: {sum_digits(1234)}")
# Output: Sum of digits in 1234: 10

print("\n===== 11. Variable Scope =====")
# Scope determines where variables can be accessed

# Global variable
global_var = "I am global"

def scope_demo():
    """Demonstrating local and global scope"""
    local_var = "I am local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

scope_demo()
# Output:
# Inside function - Local: I am local
# Inside function - Global: I am global

# print(local_var)  # This would cause NameError - local_var is not accessible outside

print("\n===== 12. Global Keyword =====")
# 'global' keyword allows modifying global variables inside functions

counter = 0

def increment():
    """Increment global counter"""
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

increment()
increment()
print(f"Counter outside function: {counter}")
# Output:
# Counter inside function: 1
# Counter inside function: 2
# Counter outside function: 2

print("\n===== 13. Nonlocal Keyword =====")
# 'nonlocal' keyword allows modifying variables in enclosing (non-global) scope

def outer_function():
    """Outer function with nested function"""
    outer_var = "outer"
    
    def inner_function():
        """Inner function using nonlocal"""
        nonlocal outer_var
        outer_var = "modified by inner"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner call: {outer_var}")
    inner_function()
    print(f"After inner call: {outer_var}")

outer_function()
# Output:
# Before inner call: outer
# Inner function: modified by inner
# After inner call: modified by inner

print("\n===== 14. Docstrings =====")
# Docstrings document functions and are accessed via __doc__

def documented_function(param1, param2):
    """
    This is a docstring.
    
    It describes what the function does.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of return value
    """
    return param1 + param2

print(documented_function.__doc__)
# Output: The docstring content as shown above

# Access docstring using help()
help(documented_function)  # Uncomment to see formatted help
# o/p => Help on function documented_function in module __main__:
# documented_function(param1, param2)
#     This is a docstring.
#     
#     It describes what the function does.
#     
#     Args:

print("\n===== 15. Function Annotations =====")
# Type hints can be added to function parameters and return values

def add_annotated(a: int, b: int) -> int:
    """Function with type annotations"""
    return a + b

result = add_annotated(5, 3)
print(f"Result: {result}")
# Output: Result: 8

# Annotations are stored in __annotations__
print(f"Annotations: {add_annotated.__annotations__}")
# Output: Annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

print("\n===== 16. Nested Functions =====")
# Functions can be defined inside other functions

def outer_func(x):
    """Outer function containing inner function"""
    def inner_func(y):
        """Inner function"""
        return y * 2
    
    result = inner_func(x)
    return result

print(f"Result: {outer_func(5)}")
# Output: Result: 10

def calculator(operation):
    """Function returning another function"""
    def add(a, b):
        return a + b
    
    def multiply(a, b):
        return a * b
    
    if operation == "add":
        return add
    elif operation == "multiply":
        return multiply

add_func = calculator("add")
print(f"Add function result: {add_func(3, 4)}")
# Output: Add function result: 7

multiply_func = calculator("multiply")
print(f"Multiply function result: {multiply_func(3, 4)}")
# Output: Multiply function result: 12

print("\n===== 17. Closures =====")
# Closure: Inner function that remembers variables from outer scope

def outer_function_closure(x):
    """Outer function creating a closure"""
    def inner_function(y):
        """Inner function accessing outer variable"""
        return x + y  # x is from outer scope
    return inner_function

closure = outer_function_closure(10)
print(f"Closure result: {closure(5)}")
# Output: Closure result: 15

def multiplier(n):
    """Create a multiplier function"""
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 5: {triple(5)}")
# Output:
# Double of 5: 10
# Triple of 5: 15

print("\n===== 18. Higher-Order Functions =====")
# Functions that take other functions as arguments or return functions

def apply_operation(func, x, y):
    """Apply a function to two arguments"""
    return func(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(f"Apply add: {apply_operation(add, 10, 5)}")
print(f"Apply subtract: {apply_operation(subtract, 10, 5)}")
# Output:
# Apply add: 15
# Apply subtract: 5

# Built-in higher-order functions
numbers = [1, 2, 3, 4, 5]

# map() - applies function to all items
squared = list(map(lambda x: x ** 2, numbers))
print(f"Mapped squares: {squared}")
# Output: Mapped squares: [1, 4, 9, 16, 25]

# filter() - filters items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered evens: {evens}")
# Output: Filtered evens: [2, 4]

# reduce() - reduces sequence to single value
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Reduced sum: {sum_all}")
# Output: Reduced sum: 15

print("\n===== 19. Decorators (Basic) =====")
# Decorators modify or enhance functions without changing their definition

def my_decorator(func):
    """Simple decorator function"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    """Function with decorator"""
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

def timing_decorator(func):
    """Decorator to measure execution time"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Function that takes time"""
    import time
    time.sleep(0.1)
    return "Done"

result = slow_function()
# Output: slow_function took 0.1001 seconds (approximately)

print("\n===== 20. Pass by Reference vs Value =====")
# Python passes arguments by object reference

def modify_list(lst):
    """Modify list (mutable object)"""
    lst.append(4)
    print(f"Inside function: {lst}")

my_list = [1, 2, 3]
modify_list(my_list)
print(f"Outside function: {my_list}")
# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]
# Note: List is modified because it's mutable

def modify_number(num):
    """Modify number (immutable object)"""
    num += 10
    print(f"Inside function: {num}")

my_num = 5
modify_number(my_num)
print(f"Outside function: {my_num}")
# Output:
# Inside function: 15
# Outside function: 5
# Note: Number is not modified because it's immutable

print("\n===== 21. Function as First-Class Objects =====")
# Functions are first-class objects: can be assigned, passed, returned

def greet(name):
    return f"Hello, {name}!"

# Assign function to variable
my_function = greet
print(my_function("Rahul"))
# Output: Hello, Rahul!

# Store functions in list
functions = [greet, len, str.upper]
print(functions[0]("Python"))
# Output: Hello, Python!

# Pass function as argument
def call_function(func, arg):
    return func(arg)

result = call_function(greet, "World")
print(result)
# Output: Hello, World!

print("\n===== 22. Important Notes =====")
print("- Functions are defined using 'def' keyword")
print("- Functions can have parameters with default values")
print("- *args collects extra positional arguments as tuple")
print("- **kwargs collects extra keyword arguments as dictionary")
print("- 'return' statement exits function and returns value")
print("- Functions without return statement return None")
print("- Recursion: function calling itself (needs base case)")
print("- 'global' keyword modifies global variables")
print("- 'nonlocal' keyword modifies enclosing scope variables")
print("- Lambda functions are anonymous single-expression functions")
print("- Functions are first-class objects in Python")
print("- Docstrings document functions (accessed via __doc__)")
print("- Decorators modify functions without changing their code")

# ================================
# End of Functions & Recursion Concepts & Examples
# ================================
