from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Complete" if self.status else "Incomplete"
        return f"{self.title} - {self.description} (Due: {self.due_date}) [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.status]


def run_todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List ---")
        print("1. Add Task\n2. Complete Task\n3. List All Tasks\n4. List Incomplete Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(Task(title, description, due_date))

        elif choice == "2":
            title = input("Enter task title to complete: ")
            if not todo.complete_task(title):
                print("Task not found.")

        elif choice == "3":
            for task in todo.list_all_tasks():
                print(task)

        elif choice == "4":
            for task in todo.list_incomplete_tasks():
                print(task)

        elif choice == "5":
            break



class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content

    def latest_posts(self, count=3):
        return self.posts[-count:]


def run_blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog System ---")
        print("1. Add Post\n2. List All Posts\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Show Latest Posts\n7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            for post in blog.list_posts():
                print(post)

        elif choice == "3":
            author = input("Author name: ")
            for post in blog.posts_by_author(author):
                print(post)

        elif choice == "4":
            title = input("Title of post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Title of post to edit: ")
            new_content = input("New Content: ")
            blog.edit_post(title, new_content)

        elif choice == "6":
            for post in blog.latest_posts():
                print(post)

        elif choice == "7":
            break


class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account: {self.acc_no}, Name: {self.name}, Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def deposit(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            acc.deposit(amount)
            return True
        return False

    def withdraw(self, acc_no, amount):
        acc = self.get_account(acc_no)
        if acc:
            return acc.withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        acc1 = self.get_account(from_acc)
        acc2 = self.get_account(to_acc)
        if acc1 and acc2:
            return acc1.transfer(acc2, amount)
        return False

    def list_accounts(self):
        return list(self.accounts.values())


def run_bank_cli():
    bank = Bank()
    while True:
        print("\n--- Banking System ---")
        print("1. Add Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Show Accounts\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            acc_no = input("Account Number: ")
            name = input("Account Holder: ")
            bank.add_account(Account(acc_no, name))

        elif choice == "2":
            acc_no = input("Account Number: ")
            amount = float(input("Amount to deposit: "))
            if not bank.deposit(acc_no, amount):
                print("Account not found.")

        elif choice == "3":
            acc_no = input("Account Number: ")
            amount = float(input("Amount to withdraw: "))
            if not bank.withdraw(acc_no, amount):
                print("Insufficient funds or account not found.")

        elif choice == "4":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount: "))
            if not bank.transfer(from_acc, to_acc, amount):
                print("Transfer failed.")

        elif choice == "5":
            for acc in bank.list_accounts():
                print(acc)

        elif choice == "6":
            break


