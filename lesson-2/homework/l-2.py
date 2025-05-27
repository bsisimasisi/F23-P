name = input("What is your name? ").strip().title()
year = int(input(f"Hey {name}, What is your year of birth? "))

age = 2025 - year
print(f"{name}, your age is {age}!")

txt = 'LMaasleitbtui'
print(txt[1::2])
txt = 'MsaatmiazD'
print(txt[0::2])

txt = "I'am John. I am from London"
print(txt.split()[-1])

txt = input("You can write anything to get it in reverse order: ")
print(txt[::-1])


text = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum value:", max(numbers))


word = input("Enter a word to check for palindrome: ").strip().lower()
if word == word[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")


email = input("Enter your email address: ").strip()
if '@' in email:
    domain = email.split('@')[-1]
    print("Domain:", domain)
else:
    print("Invalid email address.")


import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(chars, k=length))
print("Generated password:", password)
