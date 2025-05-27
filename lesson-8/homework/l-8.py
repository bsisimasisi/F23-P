try:
    num = int(input("Enter a number to divide by zero: "))
    result = num / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    value = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    raise TypeError("Both inputs must be numbers.")

try:
    with open("/root/protected.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("You do not have permission to access this file.")

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range.")

try:
    num = input("Press Ctrl+C to interrupt this input: ")
except KeyboardInterrupt:
    print("\nInput was cancelled.")

try:
    x = 1 / 0
except ArithmeticError:
    print("An arithmetic error occurred.")

try:
    with open("file_with_encoding_issue.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Cannot decode file with the given encoding.")

try:
    my_list = [1, 2, 3]
    my_list.non_existent_method()
except AttributeError:
    print("That attribute does not exist for this object.")

sample_text = """Python is fun.
File operations are useful.
We are learning exception handling and file I/O.
This is the last line."""
with open("sample.txt", "w") as f:
    f.write(sample_text)

with open("sample.txt", "r") as f:
    print(f.read())

n = 2
with open("sample.txt", "r") as f:
    for _ in range(n):
        print(f.readline(), end='')

with open("sample.txt", "a") as f:
    f.write("\nNew line added.")
with open("sample.txt", "r") as f:
    print(f.read())

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

with open("sample.txt", "r") as f:
    line_list = f.readlines()
    print(line_list)

with open("sample.txt", "r") as f:
    content = ""
    for line in f:
        content += line
    print(content)

with open("sample.txt", "r") as f:
    array = [line.strip() for line in f]
    print(array)

with open("sample.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

with open("sample.txt", "r") as f:
    print("Number of lines:", len(f.readlines()))

from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().replace(",", "").replace(".", "").split()
    frequency = Counter(words)
    print(frequency)

import os
print("File size (bytes):", os.path.getsize("sample.txt"))

my_list = ["apple", "banana", "cherry"]
with open("list_output.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")

with open("sample.txt", "r") as src, open("copy_sample.txt", "w") as dest:
    dest.write(src.read())

with open("sample.txt", "r") as f1, open("list_output.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

import random
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("Random line:", random.choice(lines).strip())

f = open("sample.txt", "r")
print("Is file closed?", f.closed)
f.close()
print("Is file closed now?", f.closed)

with open("sample.txt", "r") as f:
    clean_lines = [line.strip() for line in f]
    print(clean_lines)

with open("sample.txt", "r") as f:
    content = f.read().replace(",", "").replace(".", "")
    word_count = len(content.split())
    print("Word count:", word_count)

with open("sample.txt", "r") as f:
    chars = list(f.read())
    print(chars)

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")

letters_per_line = 5
alphabet = string.ascii_lowercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), letters_per_line):
        f.write(alphabet[i:i+letters_per_line] + "\n")
