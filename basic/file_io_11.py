# ===================================
# Python File I/O - Comprehensive Concepts and Examples
# Source: Python Official Documentation & Tutorial
# ===================================

print("===== 1. Basic File Operations =====")
# Files are used to store data persistently
# Basic operations: open, read/write, close

# Opening a file
file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, World!\n")
file.write("This is a Python file I/O tutorial.\n")
file.close()  # Always close the file when done
print("File created and written successfully!")

# Reading a file
file = open("example.txt", "r")  # Open file in read mode
content = file.read()
print(f"File content:\n{content}")
file.close()
# Output:
# File content:
# Hello, World!
# This is a Python file I/O tutorial.

print("\n===== 2. File Modes =====")
# Different modes for opening files

# 'r' - Read mode (default for text files)
# Opens file for reading, raises FileNotFoundError if file doesn't exist
file = open("example.txt", "r")
print("File opened in read mode")
file.close()

# 'w' - Write mode
# Opens file for writing, creates file if it doesn't exist, truncates if exists
file = open("write_example.txt", "w")
file.write("New content")
file.close()
print("File opened in write mode")

# 'a' - Append mode
# Opens file for appending, creates file if it doesn't exist
file = open("append_example.txt", "a")
file.write("Appended line 1\n")
file.write("Appended line 2\n")
file.close()
print("File opened in append mode")

# 'x' - Exclusive creation mode
# Creates file only if it doesn't exist, raises FileExistsError if exists
try:
    file = open("exclusive_example.txt", "x")
    file.write("This file was created exclusively")
    file.close()
    print("File created in exclusive mode")
except FileExistsError:
    print("File already exists!")

# 'b' - Binary mode (used with other modes: 'rb', 'wb', 'ab')
# Used for reading/writing binary data (images, videos, etc.)
file = open("binary_example.bin", "wb")
file.write(b"Binary data: \x00\x01\x02\x03")
file.close()
print("File opened in binary write mode")

# 't' - Text mode (default)
# Used for text files, can be combined with other modes: 'rt', 'wt', 'at'
file = open("text_example.txt", "wt")
file.write("Text mode file")
file.close()
print("File opened in text mode")

# '+' - Read and write mode (combined with other modes)
# 'r+' - Read and write (file must exist)
# 'w+' - Write and read (creates/truncates file)
# 'a+' - Append and read (creates file if doesn't exist)

file = open("readwrite_example.txt", "w+")
file.write("Initial content\n")
file.seek(0)  # Move to beginning to read
content = file.read()
print(f"Read after write: {content}")
file.close()

print("\n===== 3. Reading Files =====")
# Different methods to read file content

# Create a sample file for reading
with open("read_example.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")

# Method 1: read() - reads entire file
file = open("read_example.txt", "r")
content = file.read()
print(f"read() output:\n{content}")
file.close()

# Method 2: read(size) - reads specified number of characters
file = open("read_example.txt", "r")
first_10 = file.read(10)
print(f"read(10) output: '{first_10}'")
file.close()

# Method 3: readline() - reads one line at a time
file = open("read_example.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(f"readline() - Line 1: '{line1.strip()}'")
print(f"readline() - Line 2: '{line2.strip()}'")
file.close()

# Method 4: readlines() - reads all lines into a list
file = open("read_example.txt", "r")
lines = file.readlines()
print(f"readlines() output: {lines}")
file.close()

# Method 5: Iterating over file object (memory efficient)
print("Iterating over file:")
file = open("read_example.txt", "r")
for line_num, line in enumerate(file, 1):
    print(f"Line {line_num}: {line.strip()}")
file.close()

print("\n===== 4. Writing Files =====")
# Different methods to write to files

# Method 1: write() - writes a string
file = open("write_example.txt", "w")
file.write("First line\n")
file.write("Second line\n")
file.write("Third line\n")
file.close()
print("write() method used")

# Method 2: writelines() - writes a list of strings
file = open("writelines_example.txt", "w")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)
file.close()
print("writelines() method used")

# Method 3: Writing formatted strings
file = open("formatted_write.txt", "w")
name = "Rahul"
age = 25
file.write(f"Name: {name}, Age: {age}\n")
file.write("Formatted string written\n")
file.close()
print("Formatted strings written")

print("\n===== 5. Context Managers (with statement) =====")
# Context managers automatically close files, even if exceptions occur
# This is the recommended way to work with files

# Using 'with' statement - file automatically closes
with open("context_example.txt", "w") as file:
    file.write("This file is automatically closed\n")
    file.write("Even if an exception occurs\n")
print("File automatically closed after 'with' block")

# Reading with context manager
with open("context_example.txt", "r") as file:
    content = file.read()
    print(f"Content read: {content}")

# Multiple files with context manager
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content in file 1\n")
    f2.write("Content in file 2\n")
print("Multiple files handled with context manager")

print("\n===== 6. File Positioning =====")
# seek() and tell() methods for file positioning

with open("position_example.txt", "w+") as file:
    file.write("0123456789ABCDEF")
    
    # tell() - returns current position
    position = file.tell()
    print(f"Current position after write: {position}")
    
    # seek(offset, whence) - change file position
    # whence: 0 (start), 1 (current), 2 (end)
    file.seek(0)  # Move to beginning
    print(f"Position after seek(0): {file.tell()}")
    
    # Read from beginning
    content = file.read(5)
    print(f"Read 5 chars from start: {content}")
    
    # Move to position 10
    file.seek(10)
    print(f"Position after seek(10): {file.tell()}")
    
    # Read from position 10
    content = file.read(5)
    print(f"Read 5 chars from position 10: {content}")
    
    # Move to end
    file.seek(0, 2)  # 2 means end of file
    print(f"Position at end: {file.tell()}")

print("\n===== 7. Text vs Binary Mode =====")
# Understanding text and binary file modes

# Text mode (default) - handles encoding/decoding automatically
with open("text_file.txt", "w") as file:
    file.write("Hello, World! 🌍\n")
    file.write("Unicode characters: 中文 العربية\n")

with open("text_file.txt", "r") as file:
    content = file.read()
    print(f"Text mode read: {content}")

# Binary mode - works with bytes
with open("binary_file.bin", "wb") as file:
    file.write(b"Binary data: \x00\x01\x02\x03")
    file.write(b"\xFF\xFE\xFD")

with open("binary_file.bin", "rb") as file:
    content = file.read()
    print(f"Binary mode read: {content}")
    print(f"Binary data as hex: {content.hex()}")

# Reading text file in binary mode
with open("text_file.txt", "rb") as file:
    content = file.read()
    print(f"Text file in binary mode: {content}")

print("\n===== 8. File Encoding =====")
# Specifying encoding when working with text files

# UTF-8 encoding (default in Python 3)
with open("utf8_file.txt", "w", encoding="utf-8") as file:
    file.write("UTF-8 encoding: Hello, 世界!\n")

with open("utf8_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"UTF-8 content: {content}")

# ASCII encoding
with open("ascii_file.txt", "w", encoding="ascii") as file:
    file.write("ASCII encoding: Hello, World!\n")

# Latin-1 encoding
with open("latin1_file.txt", "w", encoding="latin-1") as file:
    file.write("Latin-1 encoding: Café\n")

print("\n===== 9. File Operations (os and os.path) =====")
# Working with file system operations

import os

# Check if file exists
if os.path.exists("example.txt"):
    print("File 'example.txt' exists")

# Get file size
if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")
    print(f"File size: {size} bytes")

# Check if path is a file
if os.path.isfile("example.txt"):
    print("'example.txt' is a file")

# Check if path is a directory
if os.path.isdir("."):
    print("'.' is a directory")

# Get absolute path
abs_path = os.path.abspath("example.txt")
print(f"Absolute path: {abs_path}")

# Get directory name
dir_name = os.path.dirname(abs_path)
print(f"Directory: {dir_name}")

# Get file name
file_name = os.path.basename(abs_path)
print(f"File name: {file_name}")

# Split path and extension
name, ext = os.path.splitext("example.txt")
print(f"Name: {name}, Extension: {ext}")

print("\n===== 10. File and Directory Operations =====")
# Creating, renaming, and deleting files

import os
import shutil

# Create a new file
with open("temp_file.txt", "w") as f:
    f.write("Temporary file content\n")

# Rename file
if os.path.exists("temp_file.txt"):
    os.rename("temp_file.txt", "renamed_file.txt")
    print("File renamed successfully")

# Copy file
if os.path.exists("renamed_file.txt"):
    shutil.copy("renamed_file.txt", "copied_file.txt")
    print("File copied successfully")

# Delete file
if os.path.exists("copied_file.txt"):
    os.remove("copied_file.txt")
    print("File deleted successfully")

# Create directory
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
    print("Directory created")

# Create nested directories
if not os.path.exists("test_dir/nested/sub"):
    os.makedirs("test_dir/nested/sub")
    print("Nested directories created")

# List directory contents
print("Directory contents:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"  File: {item}")
    elif os.path.isdir(item):
        print(f"  Directory: {item}")

# Remove directory (must be empty)
if os.path.exists("test_dir/nested/sub"):
    os.rmdir("test_dir/nested/sub")
    print("Directory removed")

# Remove directory tree
if os.path.exists("test_dir"):
    shutil.rmtree("test_dir")
    print("Directory tree removed")

print("\n===== 11. Working with Pathlib (Modern Approach) =====")
# pathlib provides object-oriented path handling (Python 3.4+)

from pathlib import Path

# Create Path object
file_path = Path("pathlib_example.txt")

# Write to file
file_path.write_text("This is written using pathlib\n")
print("File written using pathlib")

# Read from file
content = file_path.read_text()
print(f"Content read: {content}")

# Check if file exists
if file_path.exists():
    print(f"File exists: {file_path}")

# Get file info
print(f"File name: {file_path.name}")
print(f"File stem (name without extension): {file_path.stem}")
print(f"File suffix (extension): {file_path.suffix}")
print(f"Parent directory: {file_path.parent}")
print(f"Absolute path: {file_path.absolute()}")

# Create directory
dir_path = Path("pathlib_dir")
dir_path.mkdir(exist_ok=True)
print("Directory created using pathlib")

# Create file in directory
file_in_dir = dir_path / "nested_file.txt"
file_in_dir.write_text("File in directory\n")
print("File created in directory")

# List directory contents
print("Directory contents:")
for item in dir_path.iterdir():
    print(f"  {item.name}")

# Remove file
file_path.unlink()
print("File removed using pathlib")

# Remove directory
shutil.rmtree(dir_path)
print("Directory removed")

print("\n===== 12. Exception Handling with Files =====")
# Handling file-related exceptions

# FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")

# PermissionError
try:
    with open("/root/protected.txt", "w") as file:
        file.write("test")
except PermissionError as e:
    print(f"Permission denied: {e}")

# IOError (general I/O error)
try:
    with open("example.txt", "r") as file:
        content = file.read()
        # Simulate an I/O error
        file.seek(-1)  # Invalid seek
except IOError as e:
    print(f"I/O error: {e}")

# Handling multiple exceptions
try:
    with open("example.txt", "r") as file:
        content = file.read()
        result = int(content)  # May raise ValueError
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid content in file")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n===== 13. Reading Large Files Efficiently =====")
# Techniques for reading large files without loading everything into memory

# Method 1: Reading line by line (memory efficient)
with open("read_example.txt", "r") as file:
    line_count = 0
    for line in file:
        line_count += 1
        # Process line here
    print(f"Total lines processed: {line_count}")

# Method 2: Reading in chunks
def read_in_chunks(file_path, chunk_size=1024):
    """Read file in chunks"""
    with open(file_path, "r") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
chunk_count = 0
for chunk in read_in_chunks("read_example.txt", chunk_size=10):
    chunk_count += 1
    # Process chunk here
print(f"File read in {chunk_count} chunks")

# Method 3: Using readline() in a loop
with open("read_example.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        # Process line here

print("\n===== 14. Working with CSV Files =====")
# Reading and writing CSV (Comma-Separated Values) files

import csv

# Writing CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Rahul", 25, "Mumbai"])
    writer.writerow(["Priya", 23, "Delhi"])
    writer.writerow(["Ankit", 27, "Bangalore"])
print("CSV file written")

# Reading CSV file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row_num, row in enumerate(reader, 1):
        print(f"Row {row_num}: {row}")

# Writing CSV with dictionary
with open("data_dict.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Rahul", "age": 25, "city": "Mumbai"})
    writer.writerow({"name": "Priya", "age": 23, "city": "Delhi"})
print("CSV file with dictionary written")

# Reading CSV as dictionary
with open("data_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['name']}, Age: {row['age']}, City: {row['city']}")

print("\n===== 15. Working with JSON Files =====")
# Reading and writing JSON (JavaScript Object Notation) files

import json

# Writing JSON file
data = {
    "name": "Rahul",
    "age": 25,
    "city": "Mumbai",
    "hobbies": ["reading", "coding", "traveling"],
    "is_student": False
}

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)
print("JSON file written")

# Reading JSON file
with open("data.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print(f"Loaded data: {loaded_data}")

# Writing list of dictionaries to JSON
students = [
    {"name": "Rahul", "age": 25, "grade": "A"},
    {"name": "Priya", "age": 23, "grade": "B"},
    {"name": "Ankit", "age": 27, "grade": "A"}
]

with open("students.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=2)
print("List of dictionaries written to JSON")

# Reading list from JSON
with open("students.json", "r") as jsonfile:
    loaded_students = json.load(jsonfile)
    for student in loaded_students:
        print(f"Student: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# JSON string operations
json_string = json.dumps(data, indent=2)
print(f"JSON string: {json_string[:50]}...")

parsed_data = json.loads(json_string)
print(f"Parsed from string: {parsed_data['name']}")

print("\n===== 16. File Buffering =====")
# Understanding file buffering

# Unbuffered (buffer size = 0)
with open("unbuffered.txt", "w", buffering=0) as file:
    file.write("Unbuffered write\n")
    print("Unbuffered file written")

# Line buffered (buffer size = 1, only for text mode)
with open("linebuffered.txt", "w", buffering=1) as file:
    file.write("Line buffered write\n")
    print("Line buffered file written")

# Fully buffered (default, buffer size = system default)
with open("buffered.txt", "w", buffering=-1) as file:
    file.write("Fully buffered write\n")
    print("Fully buffered file written")

# Custom buffer size (in bytes)
with open("custom_buffer.txt", "w", buffering=1024) as file:
    file.write("Custom buffer size write\n")
    print("Custom buffer file written")

# Flush buffer manually
with open("flush_example.txt", "w") as file:
    file.write("Before flush\n")
    file.flush()  # Force write to disk
    file.write("After flush\n")
    print("Buffer flushed manually")

print("\n===== 17. File Attributes and Metadata =====")
# Getting file information

import os
import time
from pathlib import Path

file_path = "example.txt"

if os.path.exists(file_path):
    # Get file stats
    stat = os.stat(file_path)
    
    print(f"File size: {stat.st_size} bytes")
    print(f"Last modified: {time.ctime(stat.st_mtime)}")
    print(f"Last accessed: {time.ctime(stat.st_atime)}")
    print(f"Created: {time.ctime(stat.st_ctime)}")
    print(f"Mode (permissions): {oct(stat.st_mode)}")
    
    # Using pathlib
    path = Path(file_path)
    print(f"File exists: {path.exists()}")
    print(f"Is file: {path.is_file()}")
    print(f"Is directory: {path.is_dir()}")
    print(f"File size (pathlib): {path.stat().st_size} bytes")

print("\n===== 18. Temporary Files and Directories =====")
# Working with temporary files

import tempfile
import os

# Create temporary file
with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as temp_file:
    temp_file.write("Temporary file content\n")
    temp_file_path = temp_file.name
    print(f"Temporary file created: {temp_file_path}")

# Read temporary file
with open(temp_file_path, "r") as f:
    content = f.read()
    print(f"Temporary file content: {content}")

# Clean up
os.unlink(temp_file_path)
print("Temporary file deleted")

# Create temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory: {temp_dir}")
    temp_file_path = os.path.join(temp_dir, "temp.txt")
    with open(temp_file_path, "w") as f:
        f.write("File in temp directory\n")
    # Directory automatically deleted when exiting 'with' block
print("Temporary directory automatically deleted")

print("\n===== 19. File Compression =====")
# Working with compressed files

import gzip
import zipfile

# Writing gzip compressed file
with gzip.open("example.txt.gz", "wt") as gz_file:
    gz_file.write("This is compressed content\n")
    gz_file.write("Multiple lines of text\n")
print("Gzip file created")

# Reading gzip compressed file
with gzip.open("example.txt.gz", "rt") as gz_file:
    content = gz_file.read()
    print(f"Gzip content: {content}")

# Creating zip file
with zipfile.ZipFile("example.zip", "w") as zip_file:
    zip_file.write("example.txt")
    zip_file.write("read_example.txt")
print("Zip file created")

# Reading zip file
with zipfile.ZipFile("example.zip", "r") as zip_file:
    print("Files in zip:")
    for file_info in zip_file.namelist():
        print(f"  {file_info}")
    
    # Extract specific file
    zip_file.extract("example.txt", "extracted/")
    print("File extracted from zip")

print("\n===== 20. File Locking =====")
# Preventing multiple processes from accessing file simultaneously

import fcntl  # Unix/Linux only
import time

# Note: File locking behavior varies by OS
# On Windows, use msvcrt module instead

# Simple file locking example (Unix/Linux)
try:
    with open("locked_file.txt", "w") as file:
        try:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            file.write("Locked content\n")
            time.sleep(1)  # Simulate work
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
            print("File locked and unlocked successfully")
        except BlockingIOError:
            print("File is locked by another process")
except ImportError:
    print("fcntl not available on this platform (Windows)")

print("\n===== 21. File Iteration and Processing =====")
# Advanced file processing techniques

# Process file line by line with line numbers
with open("read_example.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        stripped_line = line.strip()
        if stripped_line:  # Skip empty lines
            print(f"Line {line_num}: {stripped_line}")

# Filter lines while reading
with open("read_example.txt", "r") as file:
    filtered_lines = [line.strip() for line in file if "Line" in line]
    print(f"Filtered lines: {filtered_lines}")

# Process file and write to another
with open("read_example.txt", "r") as input_file, \
     open("processed_output.txt", "w") as output_file:
    for line in input_file:
        processed = line.strip().upper() + "\n"
        output_file.write(processed)
print("File processed and written")

# Count words in file
word_count = 0
with open("read_example.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count += len(words)
print(f"Total words in file: {word_count}")

print("\n===== 22. File Searching and Pattern Matching =====")
# Searching for content in files

import re

# Search for pattern in file
pattern = r"Line \d+"
with open("read_example.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        matches = re.findall(pattern, line)
        if matches:
            print(f"Line {line_num}: Found {matches}")

# Search and replace in file
with open("read_example.txt", "r") as file:
    content = file.read()
    modified_content = re.sub(r"Line (\d+)", r"Line Number \1", content)

with open("modified_example.txt", "w") as file:
    file.write(modified_content)
print("File modified with pattern replacement")

# Case-insensitive search
search_term = "line"
with open("read_example.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        if search_term.lower() in line.lower():
            print(f"Found '{search_term}' in line {line_num}: {line.strip()}")

print("\n===== 23. File Validation and Error Checking =====")
# Validating files before operations

def is_valid_text_file(filepath):
    """Check if file is a valid text file"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False
    except Exception:
        return False

def is_file_readable(filepath):
    """Check if file can be read"""
    return os.path.exists(filepath) and os.access(filepath, os.R_OK)

def is_file_writable(filepath):
    """Check if file can be written"""
    if os.path.exists(filepath):
        return os.access(filepath, os.W_OK)
    else:
        # Check if directory is writable
        directory = os.path.dirname(filepath) or "."
        return os.access(directory, os.W_OK)

# Test validation functions
test_file = "example.txt"
print(f"File exists: {os.path.exists(test_file)}")
print(f"File is readable: {is_file_readable(test_file)}")
print(f"File is writable: {is_file_writable(test_file)}")
print(f"File is valid text: {is_valid_text_file(test_file)}")

print("\n===== 24. Best Practices =====")
print("1. Always use 'with' statement for file operations")
print("2. Handle exceptions (FileNotFoundError, PermissionError, etc.)")
print("3. Specify encoding explicitly for text files (utf-8 recommended)")
print("4. Use pathlib for modern path handling (Python 3.4+)")
print("5. Close files explicitly if not using 'with' statement")
print("6. Use binary mode for non-text files (images, videos, etc.)")
print("7. Read large files in chunks or line by line to save memory")
print("8. Validate file existence and permissions before operations")
print("9. Use appropriate file modes (r, w, a, x) based on needs")
print("10. Clean up temporary files after use")
print("11. Use context managers for multiple files")
print("12. Consider file locking for multi-process scenarios")
print("13. Use os.path or pathlib for cross-platform compatibility")
print("14. Handle encoding errors gracefully")
print("15. Use buffering appropriately for performance")

print("\n===== 25. Common File I/O Patterns =====")

# Pattern 1: Read all lines into list
def read_all_lines(filepath):
    """Read all lines from file"""
    with open(filepath, "r") as file:
        return file.readlines()

# Pattern 2: Read file as single string
def read_file_content(filepath):
    """Read entire file as string"""
    with open(filepath, "r") as file:
        return file.read()

# Pattern 3: Write list of lines
def write_lines(filepath, lines):
    """Write list of lines to file"""
    with open(filepath, "w") as file:
        file.writelines(lines)

# Pattern 4: Append to file
def append_to_file(filepath, content):
    """Append content to file"""
    with open(filepath, "a") as file:
        file.write(content)

# Pattern 5: Copy file
def copy_file(source, destination):
    """Copy file from source to destination"""
    shutil.copy(source, destination)

# Pattern 6: Safe file write (write to temp, then rename)
def safe_write(filepath, content):
    """Safely write to file (atomic operation)"""
    temp_path = filepath + ".tmp"
    with open(temp_path, "w") as file:
        file.write(content)
    os.rename(temp_path, filepath)

# Usage examples
if os.path.exists("read_example.txt"):
    lines = read_all_lines("read_example.txt")
    print(f"Read {len(lines)} lines")

    content = read_file_content("read_example.txt")
    print(f"File content length: {len(content)} characters")

# ================================
# End of File I/O Concepts & Examples
# ================================
