class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)

        if book is None:
            raise ValueError("Book not found")

        if not book.available:
            raise ValueError("Book is already borrowed")

        book.available = False

    def return_book(self, title):
        book = self.find_book(title)

        if book is None:
            raise ValueError("Book not found")

        if book.available:
            raise ValueError("Book was not borrowed")

        book.available = True

    def available_books(self):
        return [book.title for book in self.books if book.available]