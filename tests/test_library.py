import unittest
from unittest.mock import patch, MagicMock
from library import Library
from items.book import Book
from items.movie import Movie
from members.member import Member
from helpers import find_item_by_id

class TestLibrary(unittest.TestCase):
    "Testing library.py"

    def setUp(self):
        """Initializing an empty library on every test"""
        self.library = Library()

        self.book_id = 10
        self.movie_id = 101
        self.member_id = 123

        self.new_book = Book(self.book_id, "Harry Potter", "R.W.Rowlings", 12)
        self.new_movie = Movie(self.movie_id, "Scary Movie", "Charles", 32)
        self.new_member = Member(self.member_id, "Carl Henrique")

        self.library.add_item(self.new_book, "Book")
        self.library.add_item(self.new_movie, "Movie")
        self.library.add_member(self.new_member)

        self.book = find_item_by_id(self.library.books, self.book_id, "item_id")
        self.movie = find_item_by_id(self.library.movies, self.movie_id, "item_id")
        self.member = find_item_by_id(self.library.members, self.member_id, "member_id")

    def test_add_item(self):
        """Testing add item in library.py"""
        self.assertIn(self.book, self.library.books)
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.creator, "R.W.Rowlings")
        self.assertEqual(self.book.copies, 12)

        self.assertIn(self.movie, self.library.movies)
        self.assertEqual(self.movie.title, "Scary Movie")
        self.assertEqual(self.movie.creator, "Charles")
        self.assertEqual(self.movie.copies, 32)

    def test_add_member(self):
        """Testing add member in library.py"""
        self.assertIn(self.member, self.library.members)
        self.assertEqual(self.member.name, "Carl Henrique")

    def test_remove_item(self):
        """Testing remove item in library.py"""
        self.library.remove_item(self.book, "Book")
        self.assertNotIn(self.book, self.library.books)

        self.library.remove_item(self.movie, "Movie")
        self.assertNotIn(self.movie, self.library.movies)

    def test_remove_member(self):
        """Testing remove member in library.py"""
        self.library.remove_member(self.member)
        self.assertNotIn(self.member, self.library.members)

    @patch("builtins.print")
    def test_update_item(self, mock_print: MagicMock):
        """Testing update item in library.py"""
        self.library.update_item(self.book, "Harry Potter 2", None, None)
        self.assertEqual(self.book.title, "Harry Potter 2")
        self.assertEqual(self.book.creator, "R.W.Rowlings")
        self.assertEqual(self.book.copies, 12)

        self.library.update_item(self.movie, "Scary Movie 2", None, None)
        self.assertEqual(self.movie.title, "Scary Movie 2")
        self.assertEqual(self.movie.creator, "Charles")
        self.assertEqual(self.movie.copies, 32)

        mock_print.assert_called()
        
    @patch("builtins.print")
    def test_update_member(self, mock_print: MagicMock):
        """Testing update member in library.py"""
        self.library.update_member(self.member, "Carl H")
        self.assertEqual(self.member.name, "Carl H")

        mock_print.assert_called()

    def test_issue_item_and_return_item(self):
        """Testing issue item and return item in library.py"""
        self.library.issue_item(self.book, "Book", self.member)
        self.assertIn(self.book, self.member.borrowed_books)
        self.assertEqual(self.book.copies, 11)

        self.library.issue_item(self.movie, "Movie", self.member)
        self.assertIn(self.movie, self.member.borrowed_movies)
        self.assertEqual(self.movie.copies, 31)

        self.library.return_item(self.book, "Book", self.member)
        self.assertNotIn(self.book, self.member.borrowed_books)
        self.assertEqual(self.book.copies, 12)

        self.library.return_item(self.movie, "Movie", self.member)
        self.assertNotIn(self.movie, self.member.borrowed_movies)
        self.assertEqual(self.movie.copies, 32)

    @patch("builtins.print")
    def test_display_items(self, mock_print: MagicMock):
        """Testing display items in library.py"""
        self.library.display_items(self.book)
        self.library.display_items(self.movie)

        mock_print.assert_called()

    @patch("builtins.print")
    def test_display_members(self, mock_print: MagicMock):
        """Testing display members in library.py"""
        self.library.display_members(self.member)

        mock_print.assert_called()