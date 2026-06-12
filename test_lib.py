import unittest
from lib import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("1984", "George Orwell")
        self.library.add_book("Duna", "Frank Herbert")

    def test_add_book(self):
        self.library.add_book("Clean Code", "Robert C. Martin")

        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(self.library.books[-1].title, "Clean Code")

    def test_borrow_book(self):
        self.library.borrow_book("1984")

        self.assertFalse(self.library.find_book("1984").available)

    def test_return_book(self):
        self.library.borrow_book("1984")
        self.library.return_book("1984")

        self.assertTrue(self.library.find_book("1984").available)

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("Harry Potter")

    def test_cannot_borrow_same_book_twice(self):
        self.library.borrow_book("1984")

        with self.assertRaises(ValueError):
            self.library.borrow_book("1984")

    def test_cannot_return_book_that_was_not_borrowed(self):
        with self.assertRaises(ValueError):
            self.library.return_book("1984")

    def test_available_books(self):
        self.library.borrow_book("1984")

        self.assertEqual(self.library.available_books(), ["Duna"])


if __name__ == "__main__":
    unittest.main()