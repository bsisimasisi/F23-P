def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

even_numbers = list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1)))

if even_numbers:
    print("Even numbers:", even_numbers)
else:
    print("No even numbers found.")


a = int(input("Enter the first number again (a): "))
b = int(input("Enter the second number again (b): "))

print("Even numbers:", list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1))))