def modify_string_with_underscores(txt):
    result = []
    i = 0
    skip_next = False
    vowels = 'aeiouAEIOU'

    while i < len(txt):
        result.append(txt[i])
        if (i + 1) % 3 == 0 and txt[i] not in vowels:
            if i + 1 < len(txt) and txt[i + 1] != '_':
                result.append('_')
        i += 1
    return ''.join(result).rstrip('_')

print(modify_string_with_underscores("hello"))      
print(modify_string_with_underscores("assalom"))     
print(modify_string_with_underscores("abcabcabcdeabcdefabcdefg"))  


try:
    num_inputs = int(input("Enter a number: "))
    for number in range(num_inputs):
        print(number ** 2)
except ValueError:
    print("Invalid input. Please enter an integer.")

i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

try:
    number = int(input("Enter a number: "))
    total_sum = sum(range(1, number + 1))
    print(f"Sum is: {total_sum}")
except ValueError:
    print("Please enter a valid integer.")

try:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(number * i)
except ValueError:
    print("Please enter a valid integer.")

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

num = 75869
print(f"Number of digits: {len(str(num))}")

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

for i in range(-10, 0):
    print(i)

for i in range(5):
    print(i)
else:
    print("Done!")

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if is_prime(num):
        print(num)

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# Exercise 13: Factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")

from collections import Counter

def uncommon_elements(list1, list2):
    """
    Return elements that are not common between two lists, including duplicates.
    Parameters:
        list1 (list): First list of elements.
        list2 (list): Second list of elements.
    Returns:
        list: Elements not common to both lists.
    """
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    result = []

    for elem in counter1:
        if elem not in counter2:
            result.extend([elem] * counter1[elem])
    for elem in counter2:
        if elem not in counter1:
            result.extend([elem] * counter2[elem])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4])) 
