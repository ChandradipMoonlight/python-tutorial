# ===================================
# Python CSV & JSON File Handling - Comprehensive Concepts and Examples
# Source: Python Official Documentation & Tutorial
# ===================================

print("===== 1. Introduction to CSV Files =====")
# CSV (Comma-Separated Values) is a simple file format for storing tabular data
# Each line represents a row, and commas separate values (fields)
# CSV files are commonly used for data exchange between applications

# Basic CSV structure:
# Name,Age,City
# Rahul,25,Mumbai
# Priya,23,Delhi
# Ankit,27,Bangalore

print("CSV files store tabular data in plain text format")
print("Values are separated by commas (or other delimiters)")
print("First line often contains column headers")

print("\n===== 2. CSV Module Overview =====")
# Python's csv module provides functionality to read and write CSV files
# It handles edge cases like commas in values, quotes, etc.

import csv

print("csv module provides:")
print("- csv.reader() - for reading CSV files")
print("- csv.writer() - for writing CSV files")
print("- csv.DictReader() - for reading as dictionaries")
print("- csv.DictWriter() - for writing from dictionaries")

print("\n===== 3. Writing CSV Files - Basic =====")
# Writing CSV files using csv.writer()

# Method 1: Writing row by row
with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["Name", "Age", "City", "Grade"])
    # Write data rows
    writer.writerow(["Rahul", 25, "Mumbai", "A"])
    writer.writerow(["Priya", 23, "Delhi", "B"])
    writer.writerow(["Ankit", 27, "Bangalore", "A"])
    writer.writerow(["Sneha", 24, "Pune", "A"])

print("CSV file 'students.csv' created successfully!")

# Reading to verify
with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(f"Row: {row}")
# Output:
# Row: ['Name', 'Age', 'City', 'Grade']
# Row: ['Rahul', '25', 'Mumbai', 'A']
# Row: ['Priya', '23', 'Delhi', 'B']
# Row: ['Ankit', '27', 'Bangalore', 'A']
# Row: ['Sneha', '24', 'Pune', 'A']

print("\n===== 4. Writing Multiple Rows at Once =====")
# Using writerows() to write multiple rows

data = [
    ["Product", "Price", "Quantity"],
    ["Laptop", 50000, 10],
    ["Mouse", 500, 50],
    ["Keyboard", 1500, 30],
    ["Monitor", 15000, 15]
]

with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)  # Write all rows at once

print("Multiple rows written to 'products.csv'")

# Verify
with open("products.csv", "r") as csvfile:
    content = csvfile.read()
    print("File content:")
    print(content)

print("\n===== 5. Reading CSV Files - Basic =====")
# Reading CSV files using csv.reader()

with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read first row (header)
    print(f"Header: {header}")
    
    # Read remaining rows
    for row_num, row in enumerate(reader, start=1):
        print(f"Row {row_num}: {row}")
# Output:
# Header: ['Name', 'Age', 'City', 'Grade']
# Row 1: ['Rahul', '25', 'Mumbai', 'A']
# Row 2: ['Priya', '23', 'Delhi', 'B']
# Row 3: ['Ankit', '27', 'Bangalore', 'A']
# Row 4: ['Sneha', '24', 'Pune', 'A']

print("\n===== 6. CSV with Different Delimiters =====")
# CSV files can use different delimiters (not just commas)

# Tab-separated values (TSV)
with open("data.tsv", "w", newline="") as tsvfile:
    writer = csv.writer(tsvfile, delimiter="\t")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Rahul", 25, "Mumbai"])
    writer.writerow(["Priya", 23, "Delhi"])

print("Tab-separated file created")

# Semicolon-separated values
with open("data_semicolon.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Rahul", 25, "Mumbai"])
    writer.writerow(["Priya", 23, "Delhi"])

print("Semicolon-separated file created")

# Reading with custom delimiter
with open("data.tsv", "r") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")
    for row in reader:
        print(f"TSV Row: {row}")

print("\n===== 7. CSV with Quotes and Special Characters =====")
# CSV module handles quotes and special characters automatically

# Data with commas, quotes, and newlines
special_data = [
    ["Name", "Description", "Price"],
    ["Book", "Python Programming, 3rd Edition", 500],
    ['Pen', 'Blue ink, "Premium Quality"', 20],
    ["Notebook", "Multi-line\nDescription\nHere", 100]
]

with open("special_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)  # Quote all fields
    writer.writerows(special_data)

print("CSV with special characters created")

# Reading special data
with open("special_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(f"Row: {row}")

print("\n===== 8. CSV Quoting Options =====")
# Different quoting strategies for CSV files

# QUOTE_MINIMAL - only quote fields that need it (default)
with open("quote_minimal.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name", "Description"])
    writer.writerow(["Item1", "Simple description"])
    writer.writerow(["Item2", "Description, with comma"])

# QUOTE_ALL - quote all fields
with open("quote_all.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Description"])
    writer.writerow(["Item1", "Simple description"])

# QUOTE_NONNUMERIC - quote all non-numeric fields
with open("quote_nonnumeric.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Rahul", 25])
    writer.writerow(["Priya", 23])

# QUOTE_NONE - never quote (escape special characters)
with open("quote_none.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(["Name", "Description"])
    writer.writerow(["Item", "Description, with comma"])

print("Different quoting options demonstrated")

print("\n===== 9. CSV DictReader - Reading as Dictionaries =====")
# DictReader reads CSV rows as dictionaries with column names as keys

# First, create a CSV file
with open("employees.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Department", "Salary"])
    writer.writerow(["Rahul", "IT", 50000])
    writer.writerow(["Priya", "HR", 45000])
    writer.writerow(["Ankit", "Finance", 55000])

# Reading with DictReader
with open("employees.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['Name']}, Department: {row['Department']}, Salary: {row['Salary']}")
# Output:
# Name: Rahul, Department: IT, Salary: 50000
# Name: Priya, Department: HR, Salary: 45000
# Name: Ankit, Department: Finance, Salary: 55000

# Accessing as dictionary
with open("employees.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Employee: {row}")
        print(f"  Keys: {list(row.keys())}")
        print(f"  Values: {list(row.values())}")

print("\n===== 10. CSV DictWriter - Writing from Dictionaries =====")
# DictWriter writes dictionaries to CSV files

# Data as list of dictionaries
employees = [
    {"Name": "Rahul", "Department": "IT", "Salary": 50000},
    {"Name": "Priya", "Department": "HR", "Salary": 45000},
    {"Name": "Ankit", "Department": "Finance", "Salary": 55000},
    {"Name": "Sneha", "Department": "Marketing", "Salary": 48000}
]

with open("employees_dict.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Department", "Salary"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header row
    writer.writerows(employees)  # Write all rows

print("CSV file written from dictionaries")

# Verify
with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Employee: {row['Name']} - {row['Department']} - ${row['Salary']}")

print("\n===== 11. CSV Filtering and Processing =====")
# Filtering and processing CSV data

# Filter rows based on condition
with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    high_salary_employees = []
    for row in reader:
        if int(row["Salary"]) > 50000:
            high_salary_employees.append(row)

print("Employees with salary > 50000:")
for emp in high_salary_employees:
    print(f"  {emp['Name']}: ${emp['Salary']}")

# Count rows by department
with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    dept_count = {}
    for row in reader:
        dept = row["Department"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

print("Department count:")
for dept, count in dept_count.items():
    print(f"  {dept}: {count}")

# Calculate average salary
with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    salaries = [int(row["Salary"]) for row in reader]
    avg_salary = sum(salaries) / len(salaries) if salaries else 0
    print(f"Average salary: ${avg_salary:.2f}")

print("\n===== 12. CSV Data Conversion =====")
# Converting CSV data to different formats

# Convert CSV to list of dictionaries
def csv_to_dict_list(filename):
    """Convert CSV file to list of dictionaries"""
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

employees_list = csv_to_dict_list("employees_dict.csv")
print(f"Converted to list: {len(employees_list)} employees")
for emp in employees_list:
    print(f"  {emp}")

# Convert list of dictionaries to CSV
def dict_list_to_csv(data, filename, fieldnames=None):
    """Convert list of dictionaries to CSV file"""
    if not data:
        return
    if fieldnames is None:
        fieldnames = data[0].keys()
    
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example conversion
new_employees = [
    {"Name": "Raj", "Department": "IT", "Salary": 52000},
    {"Name": "Meera", "Department": "HR", "Salary": 46000}
]

dict_list_to_csv(new_employees, "new_employees.csv")
print("List converted to CSV file")

print("\n===== 13. CSV Error Handling =====")
# Handling errors when working with CSV files

import os

# Handle missing file
try:
    with open("nonexistent.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found: nonexistent.csv")

# Handle malformed CSV
try:
    with open("malformed.csv", "w") as f:
        f.write("Name,Age\nRahul,25\nPriya,23,Extra,Fields\n")
    
    with open("malformed.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row_num, row in enumerate(reader, start=2):
            if len(row) != len(header):
                print(f"Warning: Row {row_num} has {len(row)} fields, expected {len(header)}")
            else:
                print(f"Row {row_num}: {row}")
except Exception as e:
    print(f"Error processing CSV: {e}")

# Handle missing fields in DictReader
with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Check if required field exists
        if "Name" in row and "Salary" in row:
            print(f"Valid row: {row['Name']}")
        else:
            print(f"Invalid row: {row}")

print("\n===== 14. Introduction to JSON Files =====")
# JSON (JavaScript Object Notation) is a lightweight data interchange format
# JSON is human-readable and widely used for APIs and configuration files

# JSON supports:
# - Objects (dictionaries in Python)
# - Arrays (lists in Python)
# - Strings, numbers, booleans, null

print("JSON is a text format for storing and exchanging data")
print("JSON is language-independent and widely supported")
print("JSON is commonly used in web APIs and configuration files")

print("\n===== 15. JSON Module Overview =====")
# Python's json module provides functionality to work with JSON

import json

print("json module provides:")
print("- json.dump() - write Python object to JSON file")
print("- json.dumps() - convert Python object to JSON string")
print("- json.load() - read JSON file to Python object")
print("- json.loads() - convert JSON string to Python object")

print("\n===== 16. Writing JSON Files - Basic =====")
# Writing Python objects to JSON files

# Writing a dictionary
data = {
    "name": "Rahul",
    "age": 25,
    "city": "Mumbai",
    "is_student": False,
    "grades": [85, 90, 92]
}

with open("student.json", "w") as jsonfile:
    json.dump(data, jsonfile)

print("JSON file 'student.json' created")

# Reading to verify
with open("student.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print(f"Loaded data: {loaded_data}")
# Output: Loaded data: {'name': 'Rahul', 'age': 25, 'city': 'Mumbai', 'is_student': False, 'grades': [85, 90, 92]}

print("\n===== 17. JSON with Pretty Printing =====")
# Formatting JSON for readability using indent parameter

student_data = {
    "name": "Rahul",
    "age": 25,
    "city": "Mumbai",
    "courses": ["Python", "Java", "Database"],
    "address": {
        "street": "123 Main St",
        "zipcode": "400001"
    }
}

# Write with indentation (pretty print)
with open("student_pretty.json", "w") as jsonfile:
    json.dump(student_data, jsonfile, indent=4)

print("Pretty-printed JSON file created")

# Read and display
with open("student_pretty.json", "r") as jsonfile:
    content = jsonfile.read()
    print("Pretty JSON content:")
    print(content)

print("\n===== 18. Reading JSON Files =====")
# Reading JSON files and converting to Python objects

# Read JSON file
with open("student.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"City: {data['city']}")
    print(f"Grades: {data['grades']}")

# Read nested JSON
with open("student_pretty.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Student: {data['name']}")
    print(f"Address: {data['address']['street']}, {data['address']['zipcode']}")
    print(f"Courses: {', '.join(data['courses'])}")

print("\n===== 19. JSON String Operations =====")
# Working with JSON strings (not files)

# Convert Python object to JSON string
python_dict = {
    "name": "Priya",
    "age": 23,
    "hobbies": ["reading", "coding"]
}

json_string = json.dumps(python_dict)
print(f"JSON string: {json_string}")
# Output: JSON string: {"name": "Priya", "age": 23, "hobbies": ["reading", "coding"]}

# Pretty JSON string
pretty_json_string = json.dumps(python_dict, indent=2)
print("Pretty JSON string:")
print(pretty_json_string)

# Convert JSON string to Python object
json_str = '{"name": "Ankit", "age": 27, "city": "Bangalore"}'
python_obj = json.loads(json_str)
print(f"Python object: {python_obj}")
print(f"Name: {python_obj['name']}")

print("\n===== 20. JSON with Lists and Nested Structures =====")
# Working with complex JSON structures

# List of dictionaries
students = [
    {"name": "Rahul", "age": 25, "grade": "A"},
    {"name": "Priya", "age": 23, "grade": "B"},
    {"name": "Ankit", "age": 27, "grade": "A"}
]

with open("students_list.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=2)

print("List of students written to JSON")

# Read list
with open("students_list.json", "r") as jsonfile:
    loaded_students = json.load(jsonfile)
    for student in loaded_students:
        print(f"Student: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Nested structures
company_data = {
    "company": "Tech Corp",
    "employees": [
        {
            "id": 1,
            "name": "Rahul",
            "department": "IT",
            "projects": ["Project A", "Project B"]
        },
        {
            "id": 2,
            "name": "Priya",
            "department": "HR",
            "projects": ["Project C"]
        }
    ],
    "locations": {
        "headquarters": "Mumbai",
        "branches": ["Delhi", "Bangalore"]
    }
}

with open("company.json", "w") as jsonfile:
    json.dump(company_data, jsonfile, indent=4)

print("Complex nested JSON structure created")

# Access nested data
with open("company.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Company: {data['company']}")
    print(f"Total employees: {len(data['employees'])}")
    for emp in data['employees']:
        print(f"  {emp['name']} - {emp['department']}")

print("\n===== 21. JSON Data Types =====")
# Understanding JSON data types and Python equivalents

# JSON to Python type mapping
json_types = {
    "string": "Hello, World!",
    "number_int": 42,
    "number_float": 3.14,
    "boolean_true": True,
    "boolean_false": False,
    "null_value": None,
    "array": [1, 2, 3, 4, 5],
    "object": {"key": "value"}
}

with open("types.json", "w") as jsonfile:
    json.dump(json_types, jsonfile, indent=2)

print("JSON with different data types created")

# Read and check types
with open("types.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Data types in JSON:")
    for key, value in data.items():
        print(f"  {key}: {value} (Python type: {type(value).__name__})")

print("\n===== 22. JSON Custom Encoding and Decoding =====")
# Handling custom objects and data types

from datetime import datetime

# Custom encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Data with datetime
event_data = {
    "event": "Python Workshop",
    "date": datetime(2024, 3, 15, 10, 30),
    "attendees": 50
}

# Write with custom encoder
with open("event.json", "w") as jsonfile:
    json.dump(event_data, jsonfile, cls=DateTimeEncoder, indent=2)

print("JSON with custom encoding created")

# Custom decoder function
def datetime_decoder(dct):
    """Decode datetime strings back to datetime objects"""
    for key, value in dct.items():
        if key == "date" and isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

# Note: json.load() doesn't support custom decoders directly
# You would need to process after loading
with open("event.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Event: {data['event']}")
    print(f"Date (as string): {data['date']}")

print("\n===== 23. JSON Error Handling =====")
# Handling errors when working with JSON

# Handle invalid JSON file
try:
    with open("invalid.json", "w") as f:
        f.write("{ invalid json }")
    
    with open("invalid.json", "r") as jsonfile:
        data = json.load(jsonfile)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")

# Handle missing file
try:
    with open("nonexistent.json", "r") as jsonfile:
        data = json.load(jsonfile)
except FileNotFoundError:
    print("JSON file not found")

# Handle invalid JSON string
try:
    invalid_json = "{'name': 'Rahul'}"  # Single quotes are invalid in JSON
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Invalid JSON string: {e}")

# Handle missing keys
try:
    with open("student.json", "r") as jsonfile:
        data = json.load(jsonfile)
        # Access key that might not exist
        email = data.get("email", "Not provided")
        print(f"Email: {email}")
except KeyError as e:
    print(f"Missing key: {e}")

print("\n===== 24. JSON Filtering and Processing =====")
# Filtering and processing JSON data

# Load students data
with open("students_list.json", "r") as jsonfile:
    students = json.load(jsonfile)

# Filter students with grade 'A'
grade_a_students = [s for s in students if s["grade"] == "A"]
print("Students with grade A:")
for student in grade_a_students:
    print(f"  {student['name']}")

# Calculate average age
ages = [s["age"] for s in students]
avg_age = sum(ages) / len(ages) if ages else 0
print(f"Average age: {avg_age:.2f}")

# Group by grade
from collections import defaultdict
grade_groups = defaultdict(list)
for student in students:
    grade_groups[student["grade"]].append(student["name"])

print("Students grouped by grade:")
for grade, names in grade_groups.items():
    print(f"  Grade {grade}: {', '.join(names)}")

# Update JSON data
with open("students_list.json", "r") as jsonfile:
    students = json.load(jsonfile)

# Add new field to each student
for student in students:
    student["status"] = "Active" if student["age"] < 25 else "Senior"

# Save updated data
with open("students_updated.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=2)

print("Updated JSON file created")

print("\n===== 25. Converting CSV to JSON =====")
# Converting CSV data to JSON format

# Read CSV and convert to JSON
csv_to_json_data = []

with open("employees_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert string numbers to integers
        row["Salary"] = int(row["Salary"])
        csv_to_json_data.append(row)

# Write to JSON
with open("employees.json", "w") as jsonfile:
    json.dump(csv_to_json_data, jsonfile, indent=2)

print("CSV converted to JSON")

# Verify
with open("employees.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(f"Converted {len(data)} employees to JSON")
    for emp in data:
        print(f"  {emp['Name']}: ${emp['Salary']}")

print("\n===== 26. Converting JSON to CSV =====")
# Converting JSON data to CSV format

# Read JSON
with open("employees.json", "r") as jsonfile:
    json_data = json.load(jsonfile)

# Convert to CSV
if json_data:
    fieldnames = json_data[0].keys()
    with open("employees_from_json.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_data)

    print("JSON converted to CSV")

    # Verify
    with open("employees_from_json.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"  {row['Name']} - {row['Department']}")

print("\n===== 27. JSON Configuration Files =====")
# Using JSON for application configuration

# Create configuration file
config = {
    "app_name": "My Application",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "settings": {
        "debug": True,
        "max_connections": 100,
        "timeout": 30
    }
}

with open("config.json", "w") as jsonfile:
    json.dump(config, jsonfile, indent=4)

print("Configuration file created")

# Read and use configuration
with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)
    print(f"App: {config['app_name']} v{config['version']}")
    print(f"Database: {config['database']['host']}:{config['database']['port']}")
    print(f"Debug mode: {config['settings']['debug']}")

print("\n===== 28. JSON API Response Simulation =====")
# Simulating API responses with JSON

# Simulate API response
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Rahul", "email": "rahul@example.com"},
            {"id": 2, "name": "Priya", "email": "priya@example.com"}
        ],
        "total": 2
    },
    "message": "Users retrieved successfully"
}

# Save API response
with open("api_response.json", "w") as jsonfile:
    json.dump(api_response, jsonfile, indent=2)

print("API response saved")

# Process API response
with open("api_response.json", "r") as jsonfile:
    response = json.load(jsonfile)
    
    if response["status"] == "success":
        users = response["data"]["users"]
        print(f"Retrieved {len(users)} users:")
        for user in users:
            print(f"  {user['name']} ({user['email']})")
    else:
        print(f"Error: {response.get('message', 'Unknown error')}")

print("\n===== 29. JSON Best Practices =====")
print("1. Always use 'with' statement for file operations")
print("2. Use indent parameter for readable JSON files")
print("3. Handle JSONDecodeError when reading JSON")
print("4. Validate JSON structure before accessing nested data")
print("5. Use .get() method to safely access dictionary keys")
print("6. Specify encoding explicitly (UTF-8 is default)")
print("7. Use json.dumps() for debugging and logging")
print("8. Keep JSON structure consistent across your application")
print("9. Use meaningful key names in JSON objects")
print("10. Handle missing or null values appropriately")
print("11. Use custom encoders for non-standard types")
print("12. Validate JSON data before processing")
print("13. Use pretty printing (indent) for configuration files")
print("14. Consider using JSON Schema for validation")
print("15. Be aware of JSON size limits for large datasets")

print("\n===== 30. CSV Best Practices =====")
print("1. Always use 'newline=\"\"' when opening CSV files for writing")
print("2. Use DictReader/DictWriter for better code readability")
print("3. Handle missing or extra fields gracefully")
print("4. Specify delimiter explicitly if not using comma")
print("5. Use quoting options appropriately for your data")
print("6. Handle encoding issues (specify encoding parameter)")
print("7. Validate data types after reading CSV")
print("8. Use csv.Sniffer() to detect CSV format")
print("9. Handle empty files and missing headers")
print("10. Use context managers ('with' statement)")
print("11. Consider using pandas for complex CSV operations")
print("12. Validate row lengths match header length")
print("13. Handle special characters and quotes properly")
print("14. Use appropriate line terminators for cross-platform compatibility")
print("15. Document CSV structure and expected fields")

print("\n===== 31. CSV Sniffer - Detecting CSV Format =====")
# Automatically detecting CSV format

# Create a CSV file with unknown format
with open("unknown_format.csv", "w", newline="") as f:
    f.write("Name|Age|City\n")
    f.write("Rahul|25|Mumbai\n")
    f.write("Priya|23|Delhi\n")

# Detect format
with open("unknown_format.csv", "r") as csvfile:
    sample = csvfile.read(1024)
    csvfile.seek(0)
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    
    print(f"Detected delimiter: '{dialect.delimiter}'")
    print(f"Has header: {sniffer.has_header(sample)}")
    
    # Read with detected dialect
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        print(f"Row: {row}")

print("\n===== 32. JSON Schema Validation (Concept) =====")
# Concept of JSON schema validation (requires jsonschema library)

print("JSON Schema is a vocabulary to validate JSON documents")
print("It defines structure, data types, and constraints")
print("Example schema structure:")
schema_example = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "age"]
}

print("Schema example structure shown")
print("Note: Install 'jsonschema' library for actual validation")

print("\n===== 33. Working with Large CSV/JSON Files =====")
# Techniques for handling large files

# Streaming JSON (for large files, use ijson library)
print("For large JSON files:")
print("- Use streaming parsers (ijson library)")
print("- Process data in chunks")
print("- Avoid loading entire file into memory")

# Large CSV processing
def process_large_csv(filename, chunk_size=1000):
    """Process large CSV file in chunks"""
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                # Process chunk
                yield chunk
                chunk = []
        # Process remaining rows
        if chunk:
            yield chunk

print("Large file processing techniques demonstrated")

print("\n===== 34. Common CSV/JSON Patterns =====")

# Pattern 1: Read CSV and convert to list of dicts
def csv_to_dict_list(filename):
    """Read CSV and return list of dictionaries"""
    with open(filename, "r") as csvfile:
        return list(csv.DictReader(csvfile))

# Pattern 2: Write list of dicts to CSV
def dict_list_to_csv(data, filename):
    """Write list of dictionaries to CSV"""
    if not data:
        return
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Pattern 3: Read JSON config
def read_config(filename):
    """Read JSON configuration file"""
    with open(filename, "r") as jsonfile:
        return json.load(jsonfile)

# Pattern 4: Update JSON file
def update_json_file(filename, updates):
    """Update JSON file with new data"""
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
    data.update(updates)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)

# Pattern 5: Filter CSV rows
def filter_csv(filename, condition_func):
    """Filter CSV rows based on condition"""
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader if condition_func(row)]

print("Common patterns for CSV/JSON operations demonstrated")

print("\n===== 35. Real-World Examples =====")

# Example 1: Student grade book (CSV)
grades_data = [
    ["Student", "Math", "Science", "English"],
    ["Rahul", 85, 90, 88],
    ["Priya", 92, 87, 95],
    ["Ankit", 78, 85, 82]
]

with open("grades.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(grades_data)

# Calculate averages
with open("grades.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])
        avg = (math + science + english) / 3
        print(f"{row['Student']}: Average = {avg:.2f}")

# Example 2: Application settings (JSON)
app_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": {
        "email": True,
        "push": False
    },
    "preferences": {
        "auto_save": True,
        "backup_interval": 3600
    }
}

with open("settings.json", "w") as jsonfile:
    json.dump(app_settings, jsonfile, indent=2)

print("Real-world examples: grades.csv and settings.json created")

# ================================
# End of CSV & JSON Concepts & Examples
# ================================
