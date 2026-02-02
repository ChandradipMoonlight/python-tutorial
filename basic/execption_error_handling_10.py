# ===================================
# Python Exception & Error Handling - Comprehensive Concepts and Examples
# Source: Python Official Documentation & Tutorial
# ===================================

print("===== 1. What are Exceptions? =====")
# Exceptions are errors that occur during program execution
# They disrupt the normal flow of the program
# Python provides mechanisms to handle exceptions gracefully

# Without exception handling, errors cause program to crash
# num = 10 / 0  # This would raise ZeroDivisionError and crash the program

print("\n===== 2. Syntax Errors vs Exceptions =====")
# Syntax Errors: Errors detected by parser before execution
# Exceptions: Errors detected during execution

# Syntax Error Example (commented out to avoid actual error):
# if True
#     print("This has syntax error - missing colon")
# SyntaxError: expected ':'

# Exception Example:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
# Output: Caught ZeroDivisionError!

print("\n===== 3. Basic Try-Except Block =====")
# try-except block catches and handles exceptions

try:
    num = int("abc")  # This will raise ValueError
except ValueError:
    print("Invalid input! Cannot convert 'abc' to integer")
# Output: Invalid input! Cannot convert 'abc' to integer

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Output: Cannot divide by zero!

print("\n===== 4. Handling Multiple Exceptions =====")
# You can handle multiple exception types

def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types!"

print(f"10 / 2 = {divide_numbers(10, 2)}")
# Output: 10 / 2 = 5.0

print(f"10 / 0 = {divide_numbers(10, 0)}")
# Output: 10 / 0 = Error: Cannot divide by zero!

print(f"'10' / 2 = {divide_numbers('10', 2)}")
# Output: '10' / 2 = Error: Invalid input types!

print("\n===== 5. Single Except Block for Multiple Exceptions =====")
# Handle multiple exceptions in one except clause

try:
    value = int(input("Enter a number: "))  # Assuming user enters invalid input
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
# Output: Error occurred: invalid literal for int() with base 10: 'abc' (if invalid input)

# Example with known values:
try:
    value = 0
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
# Output: Error occurred: division by zero

print("\n===== 6. Accessing Exception Information =====")
# Use 'as' keyword to access exception object

try:
    num = int("not_a_number")
except ValueError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")
# Output:
# Exception type: ValueError
# Exception message: invalid literal for int() with base 10: 'not_a_number'
# Exception args: ("invalid literal for int() with base 10: 'not_a_number'",)

print("\n===== 7. Try-Except-Else Block =====")
# 'else' block executes if no exception occurs

def safe_divide(a, b):
    """Divide with else block"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero attempted!")
        return None
    else:
        print("Division successful!")
        return result

print(f"Result: {safe_divide(10, 2)}")
# Output:
# Division successful!
# Result: 5.0

print(f"Result: {safe_divide(10, 0)}")
# Output:
# Division by zero attempted!
# Result: None

print("\n===== 8. Try-Except-Finally Block =====")
# 'finally' block always executes, regardless of exceptions

def file_operation_example():
    """Demonstrate finally block"""
    file = None
    try:
        file = open("test_file.txt", "w")
        file.write("Hello, World!")
        result = 10 / 0  # This will raise an exception
    except ZeroDivisionError:
        print("Exception caught: Division by zero")
    finally:
        if file:
            file.close()
            print("File closed in finally block")
        print("Finally block always executes!")

file_operation_example()
# Output:
# Exception caught: Division by zero
# File closed in finally block
# Finally block always executes!

print("\n===== 9. Common Built-in Exceptions =====")
# Python has many built-in exception types

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
# Output: ZeroDivisionError: division by zero

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
# Output: ValueError: invalid literal for int() with base 10: 'abc'

# TypeError
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")
# Output: TypeError: can only concatenate str (not "int") to str

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")
# Output: IndexError: list index out of range

# KeyError
try:
    my_dict = {"name": "Rahul"}
    print(my_dict["age"])
except KeyError as e:
    print(f"KeyError: {e}")
# Output: KeyError: 'age'

# FileNotFoundError
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
# Output: FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'

# AttributeError
try:
    my_list = [1, 2, 3]
    my_list.append_item(4)  # append_item doesn't exist
except AttributeError as e:
    print(f"AttributeError: {e}")
# Output: AttributeError: 'list' object has no attribute 'append_item'

print("\n===== 10. Catching All Exceptions =====")
# Catching all exceptions (not recommended, but sometimes necessary)

try:
    result = 10 / 0
except Exception as e:
    print(f"Caught exception: {type(e).__name__} - {e}")
# Output: Caught exception: ZeroDivisionError - division by zero

# Bare except (not recommended - catches everything including SystemExit, KeyboardInterrupt)
try:
    result = int("abc")
except:  # Bare except - catches all exceptions
    print("An error occurred!")
# Output: An error occurred!

print("\n===== 11. Raising Exceptions =====")
# Use 'raise' keyword to raise exceptions explicitly

def check_age(age):
    """Check if age is valid"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be greater than 150!")
    return f"Valid age: {age}"

try:
    print(check_age(25))
    # Output: Valid age: 25
    
    print(check_age(-5))
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Age cannot be negative!

# Raising exception with custom message
try:
    raise ValueError("This is a custom error message!")
except ValueError as e:
    print(f"Caught: {e}")
# Output: Caught: This is a custom error message!

print("\n===== 12. Re-raising Exceptions =====")
# Re-raise an exception after handling it

def process_data(data):
    """Process data and re-raise exception if needed"""
    try:
        result = int(data)
    except ValueError:
        print("Error in process_data: Invalid data format")
        raise  # Re-raise the exception

try:
    process_data("abc")
except ValueError as e:
    print(f"Caught re-raised exception: {e}")
# Output:
# Error in process_data: Invalid data format
# Caught re-raised exception: invalid literal for int() with base 10: 'abc'

print("\n===== 13. Custom Exceptions =====")
# Create custom exception classes by inheriting from Exception

class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    pass

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds! Balance: ${balance}, Required: ${amount}"
        super().__init__(self.message)

def withdraw_money(balance, amount):
    """Withdraw money with custom exception"""
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    result = withdraw_money(100, 150)
except InsufficientFundsError as e:
    print(f"Custom exception: {e}")
    print(f"Balance: ${e.balance}, Amount: ${e.amount}")
# Output:
# Custom exception: Insufficient funds! Balance: $100, Required: $150
# Balance: $100, Amount: $150

print("\n===== 14. Exception Hierarchy =====")
# Exceptions form a hierarchy - catch base exceptions to catch all derived ones

try:
    result = 10 / 0
except ArithmeticError as e:  # ZeroDivisionError is a subclass of ArithmeticError
    print(f"Caught ArithmeticError: {e}")
# Output: Caught ArithmeticError: division by zero

try:
    num = int("abc")
except LookupError as e:  # This won't catch ValueError
    print(f"Caught LookupError: {e}")
except ValueError as e:  # This will catch ValueError
    print(f"Caught ValueError: {e}")
# Output: Caught ValueError: invalid literal for int() with base 10: 'abc'

# BaseException is the base class for all exceptions
print(f"ZeroDivisionError is subclass of ArithmeticError: {issubclass(ZeroDivisionError, ArithmeticError)}")
# Output: ZeroDivisionError is subclass of ArithmeticError: True

print(f"ArithmeticError is subclass of Exception: {issubclass(ArithmeticError, Exception)}")
# Output: ArithmeticError is subclass of Exception: True

print("\n===== 15. Assertions =====")
# Assertions are used for debugging - raise AssertionError if condition is False

def calculate_average(numbers):
    """Calculate average with assertion"""
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

try:
    result = calculate_average([10, 20, 30])
    print(f"Average: {result}")
    # Output: Average: 20.0
    
    result = calculate_average([])  # This will raise AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")
# Output: AssertionError: List cannot be empty!

# Assertions can be disabled with -O flag: python -O script.py

print("\n===== 16. Exception Chaining =====")
# Chain exceptions using 'from' keyword

def process_file(filename):
    """Process file with exception chaining"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            num = int(content)
    except FileNotFoundError as e:
        raise ValueError(f"Could not process file: {filename}") from e

try:
    process_file("nonexistent.txt")
except ValueError as e:
    print(f"ValueError: {e}")
    print(f"Caused by: {e.__cause__}")
# Output:
# ValueError: Could not process file: nonexistent.txt
# Caused by: [Errno 2] No such file or directory: 'nonexistent.txt'

print("\n===== 17. Context Managers and Exceptions =====")
# Context managers (with statement) handle exceptions automatically

# File operations with context manager
try:
    with open("test_output.txt", "w") as f:
        f.write("Hello, World!")
        result = 10 / 0  # Exception occurs
except ZeroDivisionError:
    print("Exception occurred, but file is automatically closed")
# Output: Exception occurred, but file is automatically closed

# File is automatically closed even if exception occurs

print("\n===== 18. Exception Handling in Functions =====")
# Functions can handle exceptions internally or let them propagate

def safe_divide(a, b):
    """Function that handles exception internally"""
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
# Output: 10 / 2 = 5.0

print(f"10 / 0 = {safe_divide(10, 0)}")
# Output: 10 / 0 = None

def divide_with_exception(a, b):
    """Function that lets exception propagate"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide_with_exception(10, 0)
except ValueError as e:
    print(f"Caught exception from function: {e}")
# Output: Caught exception from function: Cannot divide by zero!

print("\n===== 19. Nested Try-Except Blocks =====")
# Try-except blocks can be nested

def nested_exception_example():
    """Demonstrate nested exception handling"""
    try:
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("Inner: Caught ZeroDivisionError")
            raise ValueError("Converting to ValueError")
    except ValueError as e:
        print(f"Outer: Caught {type(e).__name__}: {e}")

nested_exception_example()
# Output:
# Inner: Caught ZeroDivisionError
# Outer: Caught ValueError: Converting to ValueError

print("\n===== 20. Exception Handling Best Practices =====")
# Best practices for exception handling

# 1. Be specific with exception types
def good_practice_1():
    """Specific exception handling"""
    try:
        num = int("123")
    except ValueError:  # Specific exception
        print("Invalid number format")
    except Exception:  # General fallback
        print("Unexpected error")

# 2. Don't use bare except
def good_practice_2():
    """Avoid bare except"""
    try:
        result = 10 / 0
    except ZeroDivisionError:  # Good - specific
        print("Division by zero")
    # except:  # Bad - too broad
    #     print("Error")

# 3. Use finally for cleanup
def good_practice_3():
    """Use finally for cleanup"""
    file = None
    try:
        file = open("temp.txt", "w")
        file.write("data")
    except IOError:
        print("File error")
    finally:
        if file:
            file.close()
            print("File closed")

# 4. Provide meaningful error messages
def good_practice_4(value):
    """Meaningful error messages"""
    if not isinstance(value, int):
        raise TypeError(f"Expected int, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Value must be non-negative, got {value}")

try:
    good_practice_4(-5)
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Value must be non-negative, got -5

print("\n===== 21. Exception Handling with Loops =====")
# Handle exceptions in loops to continue processing

numbers = ["10", "20", "abc", "30", "xyz", "40"]
valid_numbers = []

for num_str in numbers:
    try:
        num = int(num_str)
        valid_numbers.append(num)
        print(f"Successfully converted: {num}")
    except ValueError:
        print(f"Skipping invalid value: {num_str}")

print(f"Valid numbers: {valid_numbers}")
# Output:
# Successfully converted: 10
# Successfully converted: 20
# Skipping invalid value: abc
# Successfully converted: 30
# Skipping invalid value: xyz
# Successfully converted: 40
# Valid numbers: [10, 20, 30, 40]

print("\n===== 22. Exception Handling with User Input =====")
# Validate user input with exception handling

def get_positive_number():
    """Get positive number from user with validation"""
    while True:
        try:
            num = float(input("Enter a positive number: "))
            if num <= 0:
                raise ValueError("Number must be positive!")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return None

# Uncomment to test with actual user input:
# number = get_positive_number()
# if number:
#     print(f"You entered: {number}")

print("\n===== 23. Exception Handling in Classes =====")
# Exception handling in class methods

class BankAccount:
    """Bank account with exception handling"""
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw with exception handling"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Deposit with exception handling"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        return self.balance

try:
    account = BankAccount(100)
    print(f"Initial balance: ${account.balance}")
    # Output: Initial balance: $100
    
    account.deposit(50)
    print(f"After deposit: ${account.balance}")
    # Output: After deposit: $150
    
    account.withdraw(75)
    print(f"After withdrawal: ${account.balance}")
    # Output: After withdrawal: $75
    
    account.withdraw(100)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
# Output: Transaction failed: Insufficient funds! Balance: $75, Required: $100

print("\n===== 24. Traceback and Debugging =====")
# Understanding tracebacks for debugging

import traceback

def function_a():
    """Function that calls function_b"""
    return function_b()

def function_b():
    """Function that raises exception"""
    return 10 / 0

try:
    result = function_a()
except ZeroDivisionError:
    print("Exception occurred!")
    print("Traceback:")
    traceback.print_exc()
# Output:
# Exception occurred!
# Traceback:
# Traceback (most recent call last):
#   File "...", line ..., in function_b
#     return 10 / 0
# ZeroDivisionError: division by zero

# Get traceback as string
try:
    result = 10 / 0
except ZeroDivisionError:
    tb_str = traceback.format_exc()
    print("Traceback as string:")
    print(tb_str)

print("\n===== 25. Suppressing Exceptions =====")
# Suppress exceptions using contextlib.suppress

from contextlib import suppress

# Suppress specific exceptions
with suppress(ZeroDivisionError):
    result = 10 / 0
    print("This won't print")
print("Program continues after suppressed exception")
# Output: Program continues after suppressed exception

# Suppress multiple exceptions
with suppress(ValueError, TypeError):
    num = int("abc")
    result = "hello" + 5
print("Program continues")
# Output: Program continues

print("\n===== 26. Important Notes =====")
print("- Exceptions are errors detected during execution")
print("- Use try-except blocks to handle exceptions gracefully")
print("- Be specific with exception types (avoid bare except)")
print("- Use 'as' keyword to access exception information")
print("- 'else' block executes when no exception occurs")
print("- 'finally' block always executes for cleanup")
print("- Use 'raise' to explicitly raise exceptions")
print("- Create custom exceptions by inheriting from Exception")
print("- Exceptions form a hierarchy - catch base classes to catch derived ones")
print("- Assertions raise AssertionError if condition is False")
print("- Use exception chaining with 'from' keyword")
print("- Context managers (with statement) handle cleanup automatically")
print("- Functions can handle exceptions or let them propagate")
print("- Nested try-except blocks are allowed")
print("- Handle exceptions in loops to continue processing")
print("- Provide meaningful error messages")
print("- Use traceback module for debugging")
print("- Use contextlib.suppress to suppress specific exceptions")

# ================================
# End of Exception & Error Handling Concepts & Examples
# ================================