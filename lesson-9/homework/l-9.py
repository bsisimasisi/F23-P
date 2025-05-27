import math
from datetime import datetime

class Circle:
    """Class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of the circle."""
        return 2 * math.pi * self.radius


class Person:
    """Class representing a person with name, country, and birthdate."""

    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def get_age(self):
        """Calculate and return the age of the person."""
        today = datetime.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

class Calculator:
    """Class for basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero."

class Shape:
    """Base class for geometric shapes."""

    def area(self):
        pass

    def perimeter(self):
        pass


class CircleShape(Shape):
    """Circle subclass of Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    """Square subclass of Shape."""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    """Triangle subclass of Shape."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class BSTNode:
    """Binary Search Tree node class."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.key:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.key:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def search(self, value):
        if value == self.key:
            return True
        elif value < self.key and self.left:
            return self.left.search(value)
        elif value > self.key and self.right:
            return self.right.search(value)
        return False

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right:
            self.right.inorder()

class Stack:
    """Stack data structure using list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push item to stack."""
        self.items.append(item)

    def pop(self):
        """Pop item from stack."""
        if not self.items:
            return "Stack is empty."
        return self.items.pop()

class Node:
    """Node for LinkedList."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list class."""

    def __init__(self):
        self.head = None

    def display(self):
        """Display all nodes."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        """Insert a node at beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete node by key."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def search(self, value):
        """Search for a node by value."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

class ShoppingCart:
    """Simple shopping cart system."""

    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        """Add item to cart."""
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        """Remove item from cart."""
        if item in self.items:
            del self.items[item]
        else:
            print(f"{item} not found in cart.")

    def total(self):
        """Return total price of items."""
        return sum(self.items.values())

class StackWithDisplay:
    """Stack with push, pop, and display."""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push item onto stack."""
        self.stack.append(item)

    def pop(self):
        """Pop item from stack."""
        if not self.stack:
            return "Stack is empty."
        return self.stack.pop()

    def display(self):
        """Display stack items."""
        print("Stack contents:", self.stack)

class Queue:
    """Queue data structure using list."""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add item to queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove item from queue."""
        if not self.queue:
            return "Queue is empty."
        return self.queue.pop(0)

class BankAccount:
    """Bank account for individual user."""

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit amount to account."""
        self.balance += amount
        return f"{amount} deposited. New balance: {self.balance}"

    def withdraw(self, amount):
        """Withdraw amount from account."""
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"{amount} withdrawn. New balance: {self.balance}"

    def get_balance(self):
        """Return current balance."""
        return f"{self.name}'s balance: {self.balance}"


class Bank:
    """Bank class to manage multiple accounts."""

    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        """Add a new account."""
        self.accounts[account.name] = account

    def get_account(self, name):
        """Retrieve an account by name."""
        return self.accounts.get(name)

    def transfer(self, from_name, to_name, amount):
        """Transfer amount between two accounts."""
        from_acc = self.get_account(from_name)
        to_acc = self.get_account(to_name)
        if from_acc and to_acc and from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            return "Transfer successful"
        return "Transfer failed"