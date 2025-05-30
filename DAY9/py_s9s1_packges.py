# You're developing a Library Management System for a school or college.
# The system should :
# Track books
# Manage users (students/staff)
# Handle borrowing/returning books
# Include utility functions like date validation
# We'll break this down into packages to simulate a real-world application

from book import Book
from user import User
from utils import is_valid_date, calculate_due_date, get_current_date

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn, total_copies):
        self.books.append(Book(title, author, isbn, total_copies))

    def register_user(self, name, user_id, role):
        self.users.append(User(name, user_id, role))

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def borrow_book(self, user_id, isbn, borrow_date):
        if not is_valid_date(borrow_date):
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        user = self.find_user(user_id)
        book = self.find_book(isbn)

        if user and book:
            if user.borrow_book(book, borrow_date):
                due = calculate_due_date(borrow_date)
                print(f"Book borrowed successfully. Due on {due}.")
            else:
                print("Book not available.")
        else:
            print("User or Book not found.")

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)

        if user and book:
            if user.return_book(book):
                print("Book returned successfully.")
            else:
                print("This book was not borrowed by the user.")
        else:
            print("User or Book not found.")

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} | ISBN: {book.isbn} | Available: {book.available_copies}/{book.total_copies}")


if __name__ == "__main__":
    system = LibrarySystem()
    system.add_book("Python Programming", "John Doe", "12345", 3)
    system.register_user("Alice", "U001", "student")

    system.borrow_book("U001", "12345", get_current_date())
    system.list_books()
    system.return_book("U001", "12345")
