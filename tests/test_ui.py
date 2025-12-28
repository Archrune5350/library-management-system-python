import unittest
from unittest.mock import patch, MagicMock
from library import Library
from items.book import Book
from items.movie import Movie
from members.member import Member
from ui import clear, enter_continue, add_header, arrow, prompt_wrong_input, prompt_empty_input, check_item_exist, check_member_exist, check_library_empty, check_item_borrowed_by_member, check_item_borrowed, display_main_menu, choose_item_type, get_valid_digit, get_valid_input, get_valid_string
from helpers import find_item_by_id
class TestUI(unittest.TestCase):
    """Testing ui.py"""
    
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

    @patch("os.system")
    def test_clear(self, mock_print: MagicMock):
        """Testing clear funtion in ui.py """
        clear()
        mock_print.assert_called_once()

    @patch("builtins.input", return_value="")
    def test_enter_continue(self, mock_input: MagicMock):
        """Testing enter continue function in ui.py"""
        enter_continue()
        mock_input.assert_called_once()

    @patch("builtins.print")
    def test_arrow(self, mock_print: MagicMock):
        """Testing arrow function in ui.py"""
        arrow()
        self.assertEqual(mock_print.call_count, 9)

    @patch("builtins.print")
    def test_add_header(self, mock_print: MagicMock):
        """Testing add header function in ui.py"""
        cases = range(11)
        for option in cases:
            with self.subTest(option = cases):
                add_header(option)

        self.assertEqual(mock_print.call_count, 11)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["Carl", "Carl", ""])
    def test_prompt_wrong_input(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing prompt wrong input function in ui.py"""
        with self.subTest("Test 1: case Name, input Carl"):
            output_case_name = prompt_wrong_input("1", "Name")
            self.assertEqual(output_case_name, "Carl")
            mock_print.assert_any_call("!!! Enter a valid name !!!")
            mock_print.assert_called_once()
            mock_input.assert_called_once()
            mock_print.reset_mock()
            mock_input.reset_mock()

        with self.subTest("Test 2: case Update Name, input Carl"):
            output_case_update_name = prompt_wrong_input("1", "Update Name")
            self.assertEqual(output_case_update_name, "Carl")
            mock_print.assert_any_call("!!! Enter a valid name !!!")
            mock_print.assert_called_once()
            mock_input.assert_called_once()
            mock_print.reset_mock()
            mock_input.reset_mock()

        with self.subTest("Test 3: case Update Name, input nothing"):
            output_case_update_name_nothing = prompt_wrong_input("", "Update Name")
            self.assertFalse(output_case_update_name_nothing)
            mock_print.assert_not_called()
            mock_input.assert_not_called()

    @patch("builtins.print")
    @patch("builtins.input", return_value="Carl")
    def test_prompt_empty_input(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing prompt empty input function in ui.py"""
        output_case_name = prompt_empty_input("Name")
        self.assertEqual(output_case_name, "Carl")
        mock_print.assert_any_call("!!! Name field can't be empty !!!")
        mock_input.assert_called_once()
        mock_print.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_check_item_exist(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing check item exist function in ui.py"""
        with self.subTest("Test 1: item_type = Book, option = 1"):
            output_book = check_item_exist(self.library, self.book_id, "Book", 1)
            self.assertTrue(output_book)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ADD NEW ITEM TO LIBRARY ###")
            mock_print.assert_any_call(f"!!! The Book ID: {self.book_id}, already exists in the system !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()
        
        with self.subTest("Test 2 item exist: item_type = Book, option = 7"):
            output_book = check_item_exist(self.library, self.book_id, "Book", 7)
            self.assertTrue(output_book)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()
     
        with self.subTest("Test 2 item doesn't exist: item_type = Book, option = 7"):
            output_book_wrong = check_item_exist(self.library, self.movie_id, "Book", 7)
            self.assertFalse(output_book_wrong)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ISSUE ITEM TO A MEMBER ###")
            mock_print.assert_any_call(f"The book with Book ID: {self.movie_id} is not available")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3: item_type = Movie, option = 1"):
            output_movie = check_item_exist(self.library, self.movie_id, "Movie", 1)
            self.assertTrue(output_movie)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ADD NEW ITEM TO LIBRARY ###")
            mock_print.assert_any_call(f"!!! The Movie ID: {self.movie_id}, already exists in the system !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 item exist: item_type = Movie, option = 7"):
            output_movie = check_item_exist(self.library, self.movie_id, "Movie", 7)
            self.assertTrue(output_movie)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 item doesn't exist: item_type = Movie, option = 7"):
            output_movie_wrong = check_item_exist(self.library, self.book_id, "Movie", 7)
            self.assertFalse(output_movie_wrong)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ISSUE ITEM TO A MEMBER ###")
            mock_print.assert_any_call(f"The movie with Movie ID: {self.book_id} is not available")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_member_exist(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing check member exist function in ui.py"""
        with self.subTest("Test 1 member exist: option = 4"):
            output_add_member = check_member_exist(self.library, self.member_id, 4)
            self.assertTrue(output_add_member)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ADD NEW MEMBER TO LIBRARY ###")
            mock_print.assert_any_call(f"!!! The Member ID: {self.member_id}, already exists in the system !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 1 member doesn't exitst: option = 4"):
            output_add_member_no_member = check_member_exist(self.library, self.book_id, 4)
            self.assertFalse(output_add_member_no_member)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 member exist: option = 5"):
            output_member = check_member_exist(self.library, self.member_id, 5)
            self.assertTrue(output_member)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 member doesn't exist: option = 5"):
            output_member_no_member = check_member_exist(self.library, self.book_id, 5)
            self.assertFalse(output_member_no_member)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### REMOVE MEMBER FROM LIBRARY ###")
            mock_print.assert_any_call(f"The member with Member ID: {self.book_id} was not found")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_check_library_empty(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing check library empty function in ui.py"""
        with self.subTest("Test 1 library not empty: item_type = Book, option = 2"):
            output_books = check_library_empty(self.library, "Book", 2)
            self.assertFalse(output_books)
            
            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 library not empty: item_type = Movie, option = 2"):
            output_movies = check_library_empty(self.library, "Movie", 2)
            self.assertFalse(output_movies)

            mock_print.assert_not_called()
            mock_input.assert_not_called()
            
        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3 library not empty: item_type = Member, option = 5"):
            output_members = check_library_empty(self.library, "Member", 5)
            self.assertFalse(output_members)

            mock_print.assert_not_called()
            mock_input.assert_not_called()
            
        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 library not empty: item_type = Book, option = 7"):
            output_books_and_members = check_library_empty(self.library, "Book", 7)
            self.assertFalse(output_books_and_members)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 5 library not empty: item_type = Movie, option = 2"):
            output_movies_and_members = check_library_empty(self.library, "Movie", 7)
            self.assertFalse(output_movies_and_members)

            mock_print.assert_not_called()
            mock_input.assert_not_called()
        
        mock_print.reset_mock()
        mock_input.reset_mock()

        self.library.books.remove(self.book)
        self.library.movies.remove(self.movie)
        self.library.members.remove(self.member)

        with self.subTest("Test 1 library empty: item_type = Book, option = 2"):
            output_books_empty = check_library_empty(self.library, "Book", 2)
            self.assertTrue(output_books_empty)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### REMOVE ITEM FROM LIBRARY ###")
            mock_print.assert_any_call("!!! There are no books in the library system returning to the menu !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 library empty: item_type = Movie, option = 2"):
            output_movies_empty = check_library_empty(self.library, "Movie", 2)
            self.assertTrue(output_movies_empty)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### REMOVE ITEM FROM LIBRARY ###")
            mock_print.assert_any_call("!!! There are no movies in the library system returning to the menu !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3 library empty: item_type = Member, option = 5"):
            output_members_empty = check_library_empty(self.library, "Member", 5)
            self.assertTrue(output_members_empty)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### REMOVE MEMBER FROM LIBRARY ###")
            mock_print.assert_any_call("!!! There are no members in the library system returning to the menu !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 library empty: item_type = Book, option = 7"):
            output_books_and_members_empty = check_library_empty(self.library, "Book", 7)
            self.assertTrue(output_books_and_members_empty)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ISSUE ITEM TO A MEMBER ###")
            mock_print.assert_any_call("!!! There are no books & members in the library system returning to the menu !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 5 library empty: item_type = Movie, option = 7"):
            output_movies_and_members_empty = check_library_empty(self.library, "Movie", 7)
            self.assertTrue(output_movies_and_members_empty)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### ISSUE ITEM TO A MEMBER ###")
            mock_print.assert_any_call("!!! There are no movies & members in the library system returning to the menu !!!")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_check_item_borrowed_by_member(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing check item borrowed by member function in ui.py"""
        with self.subTest("Test 1 item not borrowed: item_type = Book, option = 8"):
            book_not_borrowed = check_item_borrowed_by_member(self.library, self.member_id, self.book_id, "Book", 8)
            self.assertFalse(book_not_borrowed)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### RETURN ITEM FROM A MEMBER ###")
            mock_print.assert_any_call(f"The Book with ID: {self.book_id}, is not borrowed by the member with ID: {self.member_id}")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 item not borrowed: item_type = Movie, option = 8"):
            movie_not_borrowed = check_item_borrowed_by_member(self.library, self.member_id, self.movie_id, "Movie", 8)
            self.assertFalse(movie_not_borrowed)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call("### RETURN ITEM FROM A MEMBER ###")
            mock_print.assert_any_call(f"The Movie with ID: {self.movie_id}, is not borrowed by the member with ID: {self.member_id}")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        self.member.borrow_item(self.book, "Book")
        self.member.borrow_item(self.movie, "Movie")

        with self.subTest("Test 3 item borrowed: item_type = Book, option = 8"):
            book_borrowed = check_item_borrowed_by_member(self.library, self.member_id, self.book_id, "Book", 8)
            self.assertTrue(book_borrowed)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 item borrowed: item_type = Movie, option = 8"):
            movie_borrowed = check_item_borrowed_by_member(self.library, self.member_id, self.movie_id, "Movie", 8)
            self.assertTrue(movie_borrowed)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_check_item_borrowed(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing check item borrowed function in ui.py"""
        with self.subTest("Test 1 item not borrowed: item_type = Book, option = 8"):
            book_not_borrowed = check_item_borrowed(self.library, self.book_id, "Book")
            self.assertFalse(book_not_borrowed)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 item not borrowed: item_type = Movie, option = 8"):
            movie_not_borrowed = check_item_borrowed(self.library, self.movie_id, "Movie")
            self.assertFalse(movie_not_borrowed)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3 item not borrowed: item_type = Member, option = 8"):
            member_has_no_borrowed_item = check_item_borrowed(self.library, self.member_id, "Member")
            self.assertFalse(member_has_no_borrowed_item)

            mock_print.assert_not_called()
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        self.member.borrow_item(self.book, "Book")
        self.member.borrow_item(self.movie, "Movie")

        with self.subTest("Test 1 item borrowed: item_type = Book, option = 8"):
            book_borrowed = check_item_borrowed(self.library, self.book_id, "Book")
            self.assertTrue(book_borrowed)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call(f"!!! The book {self.book_id} is currently borrowed by member: {self.member_id} {self.member.name} !!!")
            mock_print.assert_any_call("Return the book before removing it")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 item borrowed: item_type = Movie, option = 8"):
            movie_borrowed = check_item_borrowed(self.library, self.movie_id, "Movie")
            self.assertTrue(movie_borrowed)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call(f"!!! The movie {self.movie_id} is currently borrowed by member: {self.member_id} {self.member.name} !!!")
            mock_print.assert_any_call("Return the movie before removing it")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3 item borrowed: item_type = Member, option = 8"):
            member_has_borrowed_item = check_item_borrowed(self.library, self.member_id, "Member")
            self.assertTrue(member_has_borrowed_item)
            self.assertEqual(mock_print.call_count, 2)

            mock_print.assert_any_call(f"!!! The member {self.member_id} {self.member.name} has a borrowed item !!!")
            mock_print.assert_any_call("Return the item before removing the member")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="1")
    def test_display_main_menu(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing display main menu function in ui.py"""
        choice = display_main_menu()

        self.assertEqual(choice, "1")
        self.assertEqual(mock_print.call_count, 12)

        mock_input.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1", "2", "a", "", "0"])
    def test_choose_item_type(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing choose item type function in ui.py"""
        with self.subTest("Test 1: input 1"):
            item_type = choose_item_type(1)
            self.assertEqual(item_type, "Book")
            self.assertEqual(mock_print.call_count, 4)

            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2: input 2"):
            item_type = choose_item_type(1)
            self.assertEqual(item_type, "Movie")
            self.assertEqual(mock_print.call_count, 4)

            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 3: input a, nothing and 0"):
            item_type = choose_item_type(1)
            self.assertEqual(item_type, "Back")
            self.assertEqual(mock_print.call_count, 10)
            self.assertEqual(mock_input.call_count, 3)
            
            mock_print.assert_any_call("Please select a valid option")

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_get_valid_digit(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing get valid digit function in ui.py"""
        with self.subTest("Test 1 digit: input 1, variable_control = Copies"):
            digit = get_valid_digit("1", "Copies", 3)
            self.assertEqual(digit, 1)
            self.assertEqual(mock_print.call_count, 1)

            mock_print.assert_any_call("### UPDATE DATA ON ITEM IN LIBRARY ###")
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 string: input string and nothing, variable_control = Update Copies"):
            string = get_valid_digit("string", "Update Copies", 3)
            self.assertIsNone(string)
            self.assertEqual(mock_print.call_count, 3)

            mock_print.assert_any_call("!!! Enter a valid value for copies !!!")
            mock_input.assert_any_call("Update number of copies or press Enter to skip: ")
            mock_input.assert_called_once()

        mock_print.reset_mock()
        mock_input.reset_mock()

    @patch("builtins.print")
    @patch("builtins.input", return_value="1")
    def test_get_valid_input(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing get valid input function in ui.py"""
        output = get_valid_input(None, "Author", 1)
        self.assertEqual(output, "1")
        self.assertEqual(mock_print.call_count, 3)

        mock_print.assert_any_call("### ADD NEW ITEM TO LIBRARY ###")
        mock_print.assert_any_call("!!! Author field can't be empty !!!")
        mock_input.assert_any_call("Enter name of Author: ")
        mock_input.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", return_value="string")
    def test_get_valid_string(self, mock_input: MagicMock, mock_print: MagicMock):
        """Testing get valid string function in ui.py"""
        with self.subTest("Test 1 string: input string, variable_control = Author, option = 1"):
            string = get_valid_string("string", "Author", 1)
            self.assertEqual(string, "string")
            
            mock_print.assert_any_call("### ADD NEW ITEM TO LIBRARY ###")
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 2 digit: input 1, variable_control = Author, option = 1"):
            digit = get_valid_string("1", "Author", 1)
            self.assertEqual(digit, "string")
            self.assertEqual(mock_print.call_count, 3)

            mock_print.assert_any_call("### ADD NEW ITEM TO LIBRARY ###")
            mock_print.assert_any_call("!!! Enter a valid author !!!")
            mock_input.assert_called_once_with("Enter name of Author: ")

        mock_print.reset_mock()
        mock_input.reset_mock()
        
        with self.subTest("Test 3 nothing: input nothing, variable_control = Update Author, option = 3"):
            update_author_nothing = get_valid_string("", "Update Author", 3)
            self.assertEqual(update_author_nothing, "")

            mock_print.assert_called_once_with("### UPDATE DATA ON ITEM IN LIBRARY ###")
            mock_input.assert_not_called()

        mock_print.reset_mock()
        mock_input.reset_mock()

        with self.subTest("Test 4 digit: input 1, variable_control = Update Author, option = 3"):
            digit_update_author = get_valid_string("1", "Update Author", 3)
            self.assertEqual(digit_update_author, "string")
            self.assertEqual(mock_print.call_count, 3)

            mock_print.assert_any_call("### UPDATE DATA ON ITEM IN LIBRARY ###")
            mock_print.assert_any_call("!!! Enter a valid author !!!")
            mock_input.assert_called_once_with("Update the author or press Enter to skip: ")

        mock_print.reset_mock()
        mock_input.reset_mock()


if __name__ == "__main__":
    unittest.main()