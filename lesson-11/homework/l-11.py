# Create a virtual environment
python -m venv myenv

source myenv/bin/activate

# Install packages (example)
pip install requests numpy


import os
import math

# Custom Modules
with open("math_operations.py", "w") as f:
    f.write('''\
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
''')

with open("string_utils.py", "w") as f:
    f.write('''\
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
''')

# --- geometry package ---
os.makedirs("geometry", exist_ok=True)
with open("geometry/__init__.py", "w") as f:
    f.write('''\
from .circle import calculate_area, calculate_circumference
''')

with open("geometry/circle.py", "w") as f:
    f.write('''\
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
''')

# --- file_operations package ---
os.makedirs("file_operations", exist_ok=True)
with open("file_operations/__init__.py", "w") as f:
    f.write('''\
from .file_reader import read_file
from .file_writer import write_file
''')

with open("file_operations/file_reader.py", "w") as f:
    f.write('''\
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
''')

with open("file_operations/file_writer.py", "w") as f:
    f.write('''\
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
''')

# === Test everything ===
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

print("\n--- Math Operations ---")
print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(2, 6))
print("Divide:", divide(10, 2))
print("Divide by zero:", divide(10, 0))

print("\n--- String Utils ---")
print("Reverse:", reverse_string("hello"))
print("Vowel Count:", count_vowels("hello world"))

print("\n--- Geometry ---")
print("Area of radius 5:", calculate_area(5))
print("Circumference of radius 5:", calculate_circumference(5))

print("\n--- File Operations ---")
sample_path = "sample.txt"
write_file(sample_path, "This is a test file.")
print("File Read:", read_file(sample_path))