import unittest
from library import Library
from items.book import Book
from items.movie import Movie
from members.member import Member
from helpers import find_item_by_id, check_if_digit, check_if_nothing, check_if_string, is_item_available, is_missing, is_book_borrowed, is_movie_borrowed, has_borrowed_item, book_borrowed_by, movie_borrowed_by

class TestHelpers(unittest.TestCase):
    """Testing helpers.py"""

    def setUp(self):
        """Initializing an empty library on every test"""
        self.library = Library()

        self.book_id = 10
        self.movie_id = 101
        self.member_id = 123

        self.digit = 1
        self.string = "string"
        self.nothing = ""

        self.new_book = Book(self.book_id, "Harry Potter", "R.W.Rowlings", 12)
        self.new_movie = Movie(self.movie_id, "Scary Movie", "Charles", 32)
        self.new_member = Member(self.member_id, "Carl Henrique")

        self.library.books.append(self.new_book)
        self.library.movies.append(self.new_movie)
        self.library.members.append(self.new_member)

        self.book = find_item_by_id(self.library.books, self.book_id, "item_id")
        self.movie = find_item_by_id(self.library.movies, self.movie_id, "item_id")
        self.member = find_item_by_id(self.library.members, self.member_id, "member_id")

    def test_find_item_by_id(self):
        """Testing find item by id function in helpers.py"""
        book = find_item_by_id(self.library.books, self.book_id, "item_id")
        self.assertEqual(book, self.book)

        movie = find_item_by_id(self.library.movies, self.movie_id, "item_id")
        self.assertEqual(movie, self.movie)

        member = find_item_by_id(self.library.members, self.member_id, "member_id")
        self.assertEqual(member, self.member)

        item_doesnt_exist = find_item_by_id(self.library.books, self.movie_id, "item_id")
        self.assertIsNone(item_doesnt_exist)

    def test_check_if_digit(self):
        """Testing check if digit function in helpers.py"""
        digit = check_if_digit(self.digit)
        self.assertTrue(digit)

        string = check_if_digit(self.string)
        self.assertFalse(string)

        nothing = check_if_digit(self.nothing)
        self.assertFalse(nothing)

    def test_check_if_string(self):
        """Testing check if string function in helpers.py"""
        digit = check_if_string(self.digit)
        self.assertFalse(digit)

        string = check_if_string(self.string)
        self.assertTrue(string)

        nothing = check_if_string(self.nothing)
        self.assertFalse(nothing)

    def test_check_if_nothing(self):
        """Testing check if nothing function in helpers.py"""
        digit = check_if_nothing(self.digit)
        self.assertFalse(digit)

        string = check_if_nothing(self.string)
        self.assertFalse(string)

        nothing = check_if_nothing(self.nothing)
        self.assertTrue(nothing)

    def test_is_item_available(self):
        """Testing is item available function in helpers.py"""
        book = is_item_available(self.book)
        self.assertIsNotNone(book)
        
        no_book = is_item_available(None)
        self.assertIsNone(no_book)

        self.book.copies = 0
        no_book_copies = is_item_available(self.book)
        self.assertIsNone(no_book_copies)
        self.assertEqual(self.book.copies, 0)

        movie = is_item_available(self.movie)
        self.assertIsNotNone(movie)

        no_movie = is_item_available(None)
        self.assertIsNone(no_movie)

        self.movie.copies = 0
        no_movie_copies = is_item_available(self.movie)
        self.assertIsNone(no_movie_copies)
        self.assertEqual(self.movie.copies, 0)

    def test_is_missing(self):
        """Testing is missing function in helpers.py"""
        self.library.books.remove(self.book)

        library_empty = is_missing(self.library.books)
        self.assertTrue(library_empty)

        library_not_empty = is_missing(self.library.movies)
        self.assertFalse(library_not_empty)

    def test_is_book_borrowed(self):
        """Testing is book borrowed function in helpers.py"""
        book_not_borrowed = is_book_borrowed(self.library, self.book_id)
        self.assertFalse(book_not_borrowed)

        self.member.borrow_item(self.book, "Book")

        book_is_borrowed = is_book_borrowed(self.library, self.book_id)
        self.assertTrue(book_is_borrowed)

    def test_is_movie_borrowed(self):
        """Testing is movie borrowed function in helpers.py"""
        movie_not_borrowed = is_movie_borrowed(self.library, self.movie_id)
        self.assertFalse(movie_not_borrowed)

        self.member.borrow_item(self.movie, "Movie")

        movie_is_borrowed = is_movie_borrowed(self.library, self.movie_id)
        self.assertTrue(movie_is_borrowed)

    def test_has_borrowed_item(self):
        """Testing has borrowed item function in helpers.py"""
        no_borrowed_item = has_borrowed_item(self.member)
        self.assertFalse(no_borrowed_item)

        self.member.borrowed_books.append(self.book)

        borrowed_item = has_borrowed_item(self.member)
        self.assertTrue(borrowed_item)

    def test_book_borrowed_by(self):
        """Testing book borrowed by function in helpers.py"""
        self.member.borrow_item(self.book, "Book")
        self.member.borrow_item(self.movie, "Movie")

        member = book_borrowed_by(self.library, self.book_id)
        self.assertEqual(self.member, member)

    def test_movie_borrowed_by(self):
        """Testing movie borrowed by function in helpers.py"""
        self.member.borrow_item(self.book, "Book")
        self.member.borrow_item(self.movie, "Movie")

        member = movie_borrowed_by(self.library, self.movie_id)
        self.assertEqual(self.member, member)

if __name__ == "__main__":
    unittest.main()