
class User:
    def __init__(self, name, user_id, role):
        self.name = name
        self.user_id = user_id
        self.role = role
        self.borrowed_books = []

    def borrow_book(self, book, borrow_date):
        if book.borrow_copy():
            self.borrowed_books.append((book, borrow_date))
            return True
        return False

    def return_book(self, book):
        for b, _ in self.borrowed_books:
            if b.isbn == book.isbn:
                book.return_copy()
                self.borrowed_books.remove((b, _))
                return True
        return False