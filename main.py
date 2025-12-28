######################################################
#   11. April 2025
#   
#   Library Management System v1
#   
#   Simon Pedersen
######################################################

# Importing libraries
import ui
from library import Library
from items.book import Book
from items.movie import Movie
from members.member import Member
from helpers import find_item_by_id

# Define main function
def main():
    """Handles the main code"""
    # Set library as Library class
    library = Library()
    
    # Run loop until it is stopped
    while True:
        # Call clear function
        ui.clear()

        # Call display main menu function and store output in choice
        choice = ui.display_main_menu()

        # Call clear function
        ui.clear()

        # Match choice to the cases
        match choice:
            case "1":
                # Set option to 1
                option = 1
                # Call choose item type and store output as item type
                item_type = ui.choose_item_type(option)

                # Call add header function
                ui.add_header(option)
                
                # If item type is book
                if item_type == "Book":
                    # Set book id as the users input
                    book_id = input("Enter the Book ID: ")
                    # Set variable control as book id
                    variable_control = "Book ID"
                    
                    # Call get valid digit and store the output as book id
                    book_id = ui.get_valid_digit(book_id, variable_control, option)
                    
                    # Call add header function
                    ui.add_header(option)

                    # Call check item exist and store output as book id exist
                    book_id_exist = ui.check_item_exist(library, book_id, item_type, option)

                    # If book id exist is true then start loop over
                    if book_id_exist:
                        continue
                        
                    # Set title as the users input
                    title = input("Enter the Title: ")
                    # Set variable control as title
                    variable_control = "Title"

                    # Call get valid input and store the output as title
                    title = ui.get_valid_input(title, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Set author as the users input
                    author = input("Enter name of Author: ")
                    # Set variable control as author
                    variable_control = "Author"

                    # Call get valid string and store the output as author
                    author = ui.get_valid_string(author, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Set copies as the users input
                    copies = input("Enter number of Copies: ")
                    # Set variable control as copies
                    variable_control = "Copies"

                    # Call get valid digit and store the output as copies
                    copies = ui.get_valid_digit(copies, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Set new book as book instance with the attributes
                    new_book = Book(book_id, title, author, copies)

                    # Call library add item with new book and item type
                    library.add_item(new_book, item_type)
                    
                    # Print the book has been succesfully added
                    print("The new book has succesfully been added to the library :-)")

                    # Display the information of the new book
                    new_book.display_info()
                
                # Else if item type is movie
                elif item_type == "Movie":
                    # Set movie id as the users input
                    movie_id = input("Enter the Movie ID: ")
                    # Set variable control as movie id
                    variable_control = "Movie ID"
                    
                    # Call get valid digit and store the output as movie id
                    movie_id = ui.get_valid_digit(movie_id, variable_control, option)

                    # Call add header function
                    ui.add_header(option)
                    
                    # Call check item exist and store output as movie id exist
                    movie_id_exist = ui.check_item_exist(library, movie_id, item_type, option)

                    # If movie id exist is true then start loop over
                    if movie_id_exist:
                        continue
                    
                    # Set title as the users input
                    title = input("Enter the Title: ")
                    # Set variable control as title
                    variable_control = "Title"

                    # Call get valid input and store the output as title
                    title = ui.get_valid_input(title, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Set director as the users input
                    director = input("Enter name of Director: ")
                    # Set variable control as director
                    variable_control = "Director"

                    # Call get valid string and store the output as director
                    director = ui.get_valid_string(director, variable_control, option)

                    # Call add header function
                    ui.add_header(option)
                    
                    # Set copies as the users input
                    copies = input("Enter number of Copies: ")
                    # Set variable control as copies
                    variable_control = "Copies"

                    # Call get valid digit and store the output as copies
                    copies = ui.get_valid_digit(copies, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Set new movie as movie instance with the attributes
                    new_movie = Movie(movie_id, title, director, copies)

                    # Call library add item with new movie and item type
                    library.add_item(new_movie, item_type)

                    # Print the movie has been succesfully added
                    print("The new movie has succesfully been added to the library :-)")

                    # Display the information of the new movie
                    new_movie.display_info()

                # Call enter continue function
                ui.enter_continue()

            case "2":
                # Set option to 2
                option = 2
                # Call choose item type and store output as item type
                item_type = ui.choose_item_type(option)

                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)

                # If library empty is true then start loop over
                if  library_empty:
                    continue
                
                # If item type is book
                if item_type == "Book":
                    # Set book id as the users input
                    book_id = input("Enter the Book ID: ")
                    # Set variable control as book id
                    variable_control = "Book ID"

                    # Call get valid digit and store the output as book id
                    book_id = ui.get_valid_digit(book_id, variable_control, option)

                    # Call check item borrowed and store the output as book is borrowed
                    book_is_borrowed = ui.check_item_borrowed(library, book_id, item_type)

                    # If book is borrowed is true then start loop over
                    if book_is_borrowed:
                        continue
                    
                    # Find book instance and store as book
                    book = find_item_by_id(library.books, book_id, "item_id")

                    # If book contains anything
                    if book:
                        # Call library remove item with book and item type
                        library.remove_item(book, item_type)
                        ui.add_header(option)
                        print(f"The book with Book ID: {book_id}, has succesfully been removed from the library system.")
                    # Else print book was not found
                    else:
                        ui.add_header(option)
                        print(f"The book with Book ID: {book_id} was not found")
                
                # Else if item type is movie
                elif item_type == "Movie":
                    # Set movie id as the users input
                    movie_id = input("Enter the Movie ID: ")
                    # Set variable control as movie id
                    variable_control = "Movie ID"

                    # Call get valid digit and store the output as movie id
                    movie_id = ui.get_valid_digit(movie_id, variable_control, option)

                    # Call check item borrowed and store the output as movie is borrowed
                    movie_is_borrowed = ui.check_item_borrowed(library, movie_id, item_type)
                    
                    # If movie is borrowed is true then start loop over
                    if movie_is_borrowed:
                        continue
                    
                    # Find movie instance and store as movie
                    movie = find_item_by_id(library.movies, movie_id, "item_id")

                    # If movie contains anything
                    if movie:
                        # Call library remove item with movie and item type
                        library.remove_item(movie, item_type)
                        ui.add_header(option)
                        print(f"The movie with Movie ID: {movie_id}, has succesfully been removed from the library system.")
                    # Else print movie was not found
                    else:
                        ui.add_header(option)
                        print(f"The movie with Movie ID: {movie_id} was not found")
                
                # Call enter continue function
                ui.enter_continue()

            case "3":
                # Set option to 3
                option = 3
                # Call choose item type and store output as item type
                item_type = ui.choose_item_type(option)
                
                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)

                # If library empty is true then start loop over
                if library_empty:
                    continue
                
                # If item type is book
                if item_type == "Book":
                    # Set book id as the users input
                    book_id = input("Enter the Book ID: ")
                    # Set variable control as book id
                    variable_control = "Book ID"
                    
                    # Call get valid digit and store the output as book id
                    book_id = ui.get_valid_digit(book_id, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Find book instance and store as book
                    book = find_item_by_id(library.books, book_id, "item_id")

                    # If book contains anything
                    if book:
                        # Set new title as the users input
                        new_title = input("Update the title or press Enter to skip: ")

                        # Call add header function
                        ui.add_header(option)

                        # Set new author as the users input
                        new_author = input("Update the author or press Enter to skip: ")
                        # Set variable control as update author
                        variable_control = "Update Author"

                        # Call get valid string and store the output as new author
                        new_author = ui.get_valid_string(new_author, variable_control, option)

                        # Call add header function
                        ui.add_header(option)

                        # Set new copies as the users input
                        new_copies = input("Update number of copies or press Enter to skip: ")
                        # Set variable control as update copies
                        variable_control = "Update Copies"

                        # Call get valid digit and store the output as new copies
                        new_copies = ui.get_valid_digit(new_copies, variable_control, option)

                        # Call add header function
                        ui.add_header(option)

                        # Call library update item with book and books new attributes
                        library.update_item(book, new_title, new_author, new_copies)

                        # Print book has succesfully been updated
                        print("The book has succesfully been updated")
                    
                    # Else print the book was not found
                    else:
                        ui.add_header(option)
                        print(f"The book with Book ID: {book_id} was not found")

                # Else if item type is movie
                elif item_type == "Movie":
                    # Set movie id as the users input
                    movie_id = input("Enter the Movie ID: ")
                    # Set variable control as movie id
                    variable_control = "Movie ID"
                    
                    # Call get valid digit and store the output as movie id
                    movie_id = ui.get_valid_digit(movie_id, variable_control, option)

                    # Call add header function
                    ui.add_header(option)

                    # Find movie instance and store as movie
                    movie = find_item_by_id(library.movies, movie_id, "item_id")

                    # If movie contains anything
                    if movie:
                        # Set new title as the users input
                        new_title = input("Update the title or press Enter to skip: ")

                        # Call add header function
                        ui.add_header(option)

                        # Set new director as the users input
                        new_director = input("Update the director or press Enter to skip: ")
                        # Set variable control as update director
                        variable_control = "Update Director"

                        # Call get valid string and store the output as new director
                        new_director = ui.get_valid_string(new_director, variable_control, option)

                        # Call add header function
                        ui.add_header(option)
                        
                        # Set new copies as the users input
                        new_copies = input("Update number of copies or press Enter to skip: ")
                        # Set variable control as update copies
                        variable_control = "Update Copies"

                        # Call get valid digit and store the output as new copies
                        new_copies = ui.get_valid_digit(new_copies, variable_control, option)

                        # Call add header function
                        ui.add_header(option)

                        # Call library update item with movie and movies new attributes
                        library.update_item(movie, new_title, new_director, new_copies)

                        # Print movie has succesfully been updated
                        print("The movie has succesfully been updated")

                    # Else print the movie was not found
                    else:
                        ui.add_header(option)
                        print(f"The movie with Movie ID: {movie_id} was not found")

                # Call enter continue function
                ui.enter_continue()

            case "4":
                # Set option to 4
                option = 4

                # Call add header function
                ui.add_header(option)

                # Set member id as the users input
                member_id = input("Enter the Member ID: ")
                # Set variable control as member id
                variable_control = "Member ID"

                # Call get valid digit and store the output as member id
                member_id = ui.get_valid_digit(member_id, variable_control, option)

                # Call add header function
                ui.add_header(option)
                
                # Call check member exist and store output as member id exist
                member_id_exist = ui.check_member_exist(library, member_id, option)

                # If member id exist is true then start loop over
                if member_id_exist:
                    continue
                
                # Set name as the users input
                name = input("Enter the name of the new member: ")
                # Set variable control as name
                variable_control = "Name"
                
                # Call get valid string and store the output as name
                name = ui.get_valid_string(name, variable_control, option)

                # Set new member as member instance with the attributes
                new_member = Member(member_id, name)

                # Call library add member with new member and item type
                library.add_member(new_member)

                # Call add header function
                ui.add_header(option)

                # Print the member has been succesfully added
                print("The new member has succesfully been added to the library")

                # Display the information of the new member
                new_member.display_info()
                
                # Call enter continue function
                ui.enter_continue()

            case "5":
                # Set option to 5
                option = 5
                # Set item type as member
                item_type = "Member"

                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)

                # If library empty is true then start loop over
                if  library_empty:
                    continue
                
                # Set member id as the users input
                member_id = input("Enter the Member ID: ")
                # Set variable control as member id
                variable_control = "Member ID"
                
                # Call get valid digit and store the output as member id
                member_id = ui.get_valid_digit(member_id, variable_control, option)

                # Call check member exist and store output as member exist
                member_exist = ui.check_member_exist(library, member_id, option)

                # If member exist is false then start loop over
                if member_exist is False:
                    continue
                
                # Call check item borrowed and store the output as member have item
                member_have_item = ui.check_item_borrowed(library, member_id, item_type)

                # If member have item is true then start loop over
                if member_have_item:
                    continue
                
                # Find member instance and store as member
                member = find_item_by_id(library.members, member_id, "member_id")
                
                # If member contains anything
                if member:
                    # Call library remove member with member
                    library.remove_member(member)
                    ui.add_header(option)
                    print(f"The member with Member ID: {member_id} has succesfully been removed from the library.")
                # Else print member was not found
                else:
                    ui.add_header(option)
                    print(f"The member with Member ID: {member_id} was not found")

                # Call enter continue function
                ui.enter_continue()

            case "6":
                # Set option to 6
                option = 6
                # Set item type as member
                item_type = "Member"

                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)

                # If library empty is true then start loop over
                if  library_empty:
                    continue
                
                # Set member id as the users input
                member_id = input("Enter the Member ID: ")
                # Set variable control as member id
                variable_control = "Update Member"

                # Call add header function
                ui.add_header(option)

                # Call get valid digit and store the output as member id
                member_id = ui.get_valid_digit(member_id, variable_control, option)

                # Call check member exist and store output as member exist
                member_exist = ui.check_member_exist(library, member_id, option)

                # If member exist is false then start loop over
                if member_exist is False:
                    continue
                
                # Find member instance and store as member
                member = find_item_by_id(library.members, member_id, "member_id")

                # If member contains anything
                if member:
                    # Set new name as the users input
                    new_name = input("Update the name or press Enter to skip: ")
                    # Set variable control as update name
                    variable_control = "Update Name"

                    # Call get valid string and store the output as new name
                    new_name = ui.get_valid_string(new_name, variable_control, option)

                    # Call library update member with member and members new attributes
                    library.update_member(member, new_name)

                    # Print member has succesfully been updated
                    print("The member has succesfully been updated")

                # Else print the member was not found
                else:
                    ui.add_header(option)
                    print(f"The member with Member ID: {member_id} was not found")

                # Call enter continue function
                ui.enter_continue

            case "7":
                # Set option to 7
                option = 7
                # Call choose item type and store output as item type
                item_type = ui.choose_item_type(option)

                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)
                
                # If library empty is true then start loop over
                if  library_empty:
                    continue
                
                # Set member id as the users input
                member_id = input("Enter the Member ID: ")
                # Set member id as the users input
                variable_control = "Member ID"

                # Call add header function
                ui.add_header(option)

                # Call get valid digit and store the output as member id
                member_id = ui.get_valid_digit(member_id, variable_control, option)

                # Call check member exist and store output as member exist
                member_exist = ui.check_member_exist(library, member_id, option)

                # If member exist is false then start loop over
                if member_exist is False:
                    continue
                
                # Find member instance and store as member
                member = find_item_by_id(library.members, member_id, "member_id")

                # If item type is book
                if item_type == "Book":
                    # Set book id as the users input
                    book_id = input("Enter the Book ID: ")
                    # Set variable control as book id
                    variable_control = "Book ID"

                    # Call get valid digit and store the output as book id
                    book_id = ui.get_valid_digit(book_id, variable_control, option)

                    # Call check item exist and store output as book exist
                    book_exist = ui.check_item_exist(library, book_id, item_type, option)

                    # If book exist is false then start loop over
                    if book_exist is False:
                        continue
                    
                    # Find book instance and store as book
                    book = find_item_by_id(library.books, book_id, "item_id")

                    # Call library issue item with book, item type and member
                    library.issue_item(book, item_type, member)

                    # Print the book has been issued
                    print(f"The book with Book ID: {book.item_id}, Title: {book.title} Author: {book.creator}, is borrowed by Member ID: {member.member_id}, name: {member.name}")

                # Else if item type is movie
                elif item_type == "Movie":
                    # Set movie id as the users input
                    movie_id = input("Enter the Movie ID: ")
                    # Set variable control as movie id
                    variable_control = "Movie ID"

                    # Call get valid digit and store the output as movie id
                    movie_id = ui.get_valid_digit(movie_id, variable_control, option)

                    # Call check item exist and store output as movie exist
                    movie_exist = ui.check_item_exist(library, movie_id, item_type, option)

                    # If movie exist is false then start loop over
                    if movie_exist is False:
                        continue
                    
                    # Find movie instance and store as book
                    movie = find_item_by_id(library.movies, movie_id, "item_id")

                    # Call library issue item with movie, item type and member
                    library.issue_item(movie, item_type, member)

                    # Print the book has been issued
                    print(f"The movie with Movie ID: {movie.item_id}, Title: {movie.title} Author: {movie.creator}, has now been borrowed by Member ID: {member.member_id}, name: {member.name}")

                # Call enter continue function
                ui.enter_continue()

            case "8":
                # Set option to 8
                option = 8
                # Call choose item type and store output as item type
                item_type = ui.choose_item_type(option)

                # Call add header function
                ui.add_header(option)

                # Call check library empty and store output as library empty
                library_empty = ui.check_library_empty(library, item_type, option)

                # If member exist is false then start loop over
                if library_empty:
                    continue
                
                # Set member id as the users input
                member_id = input("Enter the Member ID: ")
                # Set member id as the users input
                variable_control = "Member ID"

                # Call get valid digit and store the output as member id
                member_id = ui.get_valid_digit(member_id, variable_control, option)

                # Call check member exist and store output as member exist
                member_exist = ui.check_member_exist(library, member_id, option)

                # If member exist is false then start loop over
                if member_exist is False:
                    continue
                
                # Find member instance and store as member
                member = find_item_by_id(library.members, member_id, "member_id")

                # If item type is book
                if item_type == "Book":
                    # Set book id as the users input
                    book_id = input("Enter the Book ID: ")
                    # Set variable control as book id
                    variable_control = "Book ID"

                    # Call get valid digit and store the output as book id
                    book_id = ui.get_valid_digit(book_id, variable_control, option)

                    # Call check item exist and store output as book exist
                    book_exist = ui.check_item_exist(library, book_id, item_type, option)
                    
                    # If book exist is false then start loop over
                    if book_exist is False:
                        continue
                    
                    # Call check item borrowed by member and store output as book is borrowed
                    book_is_borrowed = ui.check_item_borrowed_by_member(library, member_id, book_id, item_type, option)

                    # If book is borrowed is false then start loop over
                    if book_is_borrowed is False:
                        continue
                    
                    # Find book instance and store as book
                    book = find_item_by_id(member.borrowed_books, book_id, "item_id")

                    # Call library return item with movie, item type and member
                    library.return_item(book, item_type, member)

                    # Print the book has been returned
                    print(f"The book with Book ID: {book.item_id}, Title: {book.title} Author: {book.creator}, has now been returned by Member ID: {member.member_id}, name: {member.name}")

                # Else if item type is movie
                elif item_type == "Movie":
                    # Set movie id as the users input
                    movie_id = input("Enter the Movie ID: ")
                    # Set variable control as movie id
                    variable_control = "Movie ID"

                    # Call get valid digit and store the output as movie id
                    movie_id = ui.get_valid_digit(movie_id, variable_control, option)

                    # Call check item exist and store output as movie exist
                    movie_exist = ui.check_item_exist(library, movie_id, item_type, option)

                    # If movie is borrowed is false then start loop over
                    if movie_exist is False:
                        continue
                    
                    # Call check item borrowed by member and store output as movie is borrowed
                    movie_is_borrowed = ui.check_item_borrowed_by_member(library, member_id, movie_id, item_type, option)

                    # If movie is borrowed is false then start loop over
                    if movie_is_borrowed is False:
                        continue
                    
                    # Find movie instance and store as movie
                    movie = find_item_by_id(member.borrowed_movies, movie_id, "item_id")

                    # Call library return item with movie, item type and member
                    library.return_item(movie, item_type, member)

                    # Print the book has been returned
                    print(f"The movie with Movie ID: {movie.item_id}, Title: {movie.title} Director: {movie.creator}, has now been returned by Member ID: {member.member_id}, name: {member.name}")

                # Call enter continue function
                ui.enter_continue()

            case "9":
                # Set option to 9
                option = 9

                # Call add header function
                ui.add_header(option)

                # Print books 
                print("\nBooks:")

                # If list of books contains anything
                if library.books:
                    # For all books in the list of books
                    for book in library.books:
                        # Call library display items with book
                        library.display_items(book)
                # Else print there are no books
                else:
                    print("There are no books in the library")
                
                # Print movies
                print("\nMovies:")
                
                # If list of movies contains anything
                if library.movies:
                    # For all movies in the list of movies
                    for movie in library.movies:
                        # Call library display items with movie
                        library.display_items(movie)
                # Else print there are no movies
                else:
                    print("There are no movies in the library")

                # Call enter continue function
                ui.enter_continue()

            case "10":
                # Set option to 10
                option = 10

                # Call add header function
                ui.add_header(option)

                # Print members
                print("\nMembers:")
                
                # For all members in the list of members
                for member in library.members:
                    # Call library display members with member
                    library.display_members(member)

                # Call enter continue function
                ui.enter_continue()

            case "0":
                # Print exiting the system
                print("Exiting the system...")
                
                # Call clear function
                ui.clear()

                # Exit the program
                break

            case _:
                # Set option to 10
                option = 0

                # Call add header function
                ui.add_header(option)

                # Print select valid option
                print("Please select a valid option")

                # Call enter continue function
                ui.enter_continue()
            
if __name__ == "__main__":
    main()