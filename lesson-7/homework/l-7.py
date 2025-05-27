def is_prime(num):
    """
    Determines if the given number is a prime number.
    Returns True if prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("What is n? "))
    print(is_prime(n))
except ValueError:
    print("n is not an integer.")
    
def digit_sum(k):
    """
    Returns the sum of the digits of a non-negative integer k.
    """
    string = str(k)
    listed = list(string)
    int_list = [int(x) for x in listed]
    return sum(int_list)

try:
    k = int(input("What number do you have in mind? "))
    result = digit_sum(k)
    print(f"The sum of the digits is {result}")
except ValueError:
    print("You are not giving a valid number.")

def powers_of_two(n):
    """
    Prints all powers of 2 (2^k) less than or equal to n.
    """
    k = 1
    while 2**k <= n:
        print(2**k)
        k += 1
try:
    n = int(input("What is n? "))
    powers_of_two(n)
except ValueError:
    print("N is not an integer")
