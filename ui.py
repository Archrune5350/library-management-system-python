######################################################
#
#   
#
#
#
######################################################

# Importing libraries
import os
from helpers import check_if_digit, check_if_string, check_if_nothing, is_item_available, is_book_borrowed, is_movie_borrowed, has_borrowed_item, is_missing, find_item_by_id, book_borrowed_by, movie_borrowed_by

# Define clear function that clears the terminal window
def clear():
    os.system('cls')

# Define enter continue function
def enter_continue():
    """Continues after enter is pressed"""
    input("Press Enter to continue...")

# Define add header function
def add_header(option):
    """Update the terminal display with header of current action"""
    # Call clear function
    clear()

    # Match option to the cases
    match option:
        case 0:
            print("### LIBRARY MANAGEMENT SYSTEM ###")
        case 1:
            print("### ADD NEW ITEM TO LIBRARY ###")
        case 2:
            print("### REMOVE ITEM FROM LIBRARY ###")
        case 3:
            print("### UPDATE DATA ON ITEM IN LIBRARY ###")
        case 4:
            print("### ADD NEW MEMBER TO LIBRARY ###")
        case 5:
            print("### REMOVE MEMBER FROM LIBRARY ###")
        case 6:
            print("### UPDATE DATA ON MEMBER OF LIBRARY ###")
        case 7:
            print("### ISSUE ITEM TO A MEMBER ###")
        case 8:
            print("### RETURN ITEM FROM A MEMBER ###")
        case 9:
            print("### DISPLAY ALL ITEMS IN LIBRARY ###")
        case 10:
            print("### DISPLAY ALL MEMBERS OF LIBRARY ###")

# Define arrow function
def arrow():
    """Prints an arrow"""
    print("                 |   ")
    print("                 |   ")
    print("                 |   ")
    print("                 |   ")
    print("                 |   ")
    print("              \  |  /")
    print("               \ | / ")
    print("                \ /  ")
    print("                 V   ")

# Define prompt wrong input function
def prompt_wrong_input(user_input, variable_control):
    """Handles error messages depending on the action"""
    # Match variable control to the cases
    match variable_control:
        # Normal cases displays error message and return new input from user
        case "Book ID":
            print("!!! Enter a valid Book ID !!!")
            user_input = input("Enter the Book ID: ")
            return user_input
        case "Author":
            print("!!! Enter a valid author !!!")
            user_input = input("Enter name of Author: ")
            return user_input
        case "Movie ID":
            print("!!! Enter a valid Movie ID !!!")
            user_input = input("Enter the Movie ID: ")
            return user_input
        case "Director":
            print("!!! Enter a valid instructor !!!")
            user_input = input("Enter name of instructor: ")
            return user_input
        case "Copies":
            print("!!! Enter a valid value for copies !!!")
            user_input = input("Enter number of Copies: ")
            return user_input
        case "Member ID":
            print("!!! Enter a valid Member ID !!!")
            user_input = input("Enter the Member ID: ")
            return user_input
        case "Name":
            print("!!! Enter a valid name !!!")
            user_input = input("Enter the name of the new member: ")
            return user_input
        
        # Update cases display error message and return new input from user, if current user input contain something
        # Else return false
        case "Update Author":
            if user_input:
                print("!!! Enter a valid author !!!")
                user_input = input("Update the author or press Enter to skip: ")
                return user_input
            else:
                return False 
        case "Update Director":
            if user_input:
                print("!!! Enter a valid instructor !!!")
                user_input = input("Update the instructor or press Enter to skip: ")
                return user_input
            else:
                return False 
        case "Update Copies":
            if user_input:
                print("!!! Enter a valid value for copies !!!")
                user_input = input("Update number of copies or press Enter to skip: ")
                return user_input
            else:
                return False
        case "Update Name":
            if user_input:
                print("!!! Enter a valid name !!!")
                user_input = input("Update the name or press Enter to skip: ")
                return user_input
            else:
                return False

# Define prompt empty input function
def prompt_empty_input(variable_control):
    """Handles empty error messages depending on the action"""
    # Match variable control to the cases
    match variable_control:
        # cases displays empty error message and return new input from user
        case "Title":
            print("!!! Title field can't be empty !!!")
            user_input = input("Enter the Title: ")
            return user_input
        case "Author":
            print("!!! Author field can't be empty !!!")
            user_input = input("Enter name of Author: ")
            return user_input
        case "Director":
            print("!!! Director field can't be empty !!!")
            user_input = input("Enter name of the Director: ")
            return user_input
        case "Name":
            print("!!! Name field can't be empty !!!")
            user_input = input("Enter the name of the new member: ")
            return user_input

# Define check item exist function
def check_item_exist(library, item_id, item_type, option):
    """Checks if an item exist with item id"""
    # If item type is book
    if item_type == "Book":
        # Find book instance and store in book
        book = find_item_by_id(library.books, item_id, "item_id")

        # Find out if the book is available
        book_available = is_item_available(book)

        # If option is 1 and book is not none
        if option == 1 and book is not None:
            # Print book id already exist in the system and return true
            add_header(option)
            print(f"!!! The Book ID: {item_id}, already exists in the system !!!")
            enter_continue()
            return True

        # If option is 7
        if option == 7:
            # If book is available return true
            if book_available:
                return True
            # Else print book is not available and return false
            add_header(option)
            print(f"The book with Book ID: {item_id} is not available")
            enter_continue()
        
        # If option is 8 and book is not none return true
        if option == 8:
            if book is not None:
                return True
            else:
                # Else print book was not found and return false
                add_header(option)
                print(f"The book with Book ID: {item_id} was not found")
                enter_continue()      
        # Else return false
        return False
    
    # Else if item type is movie
    elif item_type == "Movie":
        # Find movie instance and store in movie
        movie = find_item_by_id(library.movies, item_id, "item_id")

        # Find out if the movie is available
        movie_available = is_item_available(movie)

        # If option is 1 and movie is not none
        if option == 1 and movie is not None:
            # Print movie id already exist in the system and return true
            add_header(option)
            print(f"!!! The Movie ID: {item_id}, already exists in the system !!!")
            enter_continue()
            return True
        
        # If option is 7
        if option == 7:
            # If movie is available return true
            if movie_available:
                return True
            # Else print movie is not available and return false
            add_header(option)
            print(f"The movie with Movie ID: {item_id} is not available")
            enter_continue()
        
        # If option is 8 and movie is not none return true
        if option == 8 and movie is not None:
            if movie is not None:
                return True
            else:
                # Else print movie was not found and return false
                add_header(option)
                print(f"The movie with Movie ID: {item_id} was not found")
                enter_continue()
        # Else return false
        return False

# Define check member exist function
def check_member_exist(library, member_id, option):
    """Checks if a member exist with member id"""
    # Find member instance and store in member
    member = find_item_by_id(library.members, member_id, "member_id")

    # If option is 4
    if option == 4:
        # If member exist
        if member:
            # Print the member already exists and return true
            add_header(option)
            print(f"!!! The Member ID: {member_id}, already exists in the system !!!")
            enter_continue()
            return True
        # Else return false
        return False
    
    # If member exist return true
    if member:
        return True
    # Else print the member was not found and return false
    add_header(option)
    print(f"The member with Member ID: {member_id} was not found")
    enter_continue()
    return False

# Define check library empty function
def check_library_empty(library, item_type, option):
    """Checks if the library is empty"""
    # If option is 7 or 8
    if option == 7 or option == 8:
        #Add Member to the item type string
        item_type = f"{item_type} & Member"

    # Checks if all lists contains anything and store in variable
    no_books = is_missing(library.books)
    no_movies = is_missing(library.movies)
    no_members = is_missing(library.members)

    # If item type is book
    if item_type == "Book":
        # If no books is true
        if no_books:
            # Print there are no books in the system and return true
            add_header(option)
            print("!!! There are no books in the library system returning to the menu !!!")
            enter_continue()
            return True
        # Else return false
        return False
    
    # If item type is movie
    if item_type == "Movie":
        # If no movies is true
        if no_movies:
            # Print there are no movies in the system and return true
            add_header(option)
            print("!!! There are no movies in the library system returning to the menu !!!")
            enter_continue()
            return True
        # Else return false
        return False
    
    # If item type is member
    if item_type == "Member":
        # If no members is true
        if no_members:
            # Print there are no members in the system and return true
            add_header(option)
            print("!!! There are no members in the library system returning to the menu !!!")
            enter_continue()
            return True
        # Else return false
        return False
    
    # If item type is book & member
    if item_type == "Book & Member":
        # If no books and no members is false return false
        if no_books and no_members is False:
            return False
        
        # If no books is true and no members is false
        if no_books is True and no_members is False:
            # Print there are no books in the system and return true
            add_header(option)
            print("!!! There are no books in the library system returning to the menu !!!")
            enter_continue()
            return True
        
        # If no books is false and no members is true
        if no_books is False and no_members is True:
            # Print there are no members in the system and return true
            add_header(option)
            print("!!! There are no members in the library system returning to the menu !!!")
            enter_continue()
            return True
        
        # If no books and no members is true
        if no_books and no_members:
            # Print there are no books & members in the system and return true
            add_header(option)
            print("!!! There are no books & members in the library system returning to the menu !!!")
            enter_continue()
            return True
    
    # If item type is movie & member
    if item_type == "Movie & Member":
        # If no movies and no members is false return false
        if no_movies and no_members is False:
            return False
        
        # If no movies is true and no members is false
        if no_movies is True and no_members is False:
            # Print there are no movies in the system and return true
            add_header(option)
            print("!!! There are no movies in the library system returning to the menu !!!")
            enter_continue()
            return True
        
        # If no movies is false and no members is true
        if no_movies is False and no_members is True:
            # Print there are no members in the system and return true
            add_header(option)
            print("!!! There are no members in the library system returning to the menu !!!")
            enter_continue()
            return True
        
        # If no movies and no members is true
        if no_movies and no_members:
            # Print there are no movies & members in the system and return true
            add_header(option)
            print("!!! There are no movies & members in the library system returning to the menu !!!")
            enter_continue()
            return True

# Define check item borrowed by member function
def check_item_borrowed_by_member(library, member_id, item_id, item_type, option):
    """Checks if an item is borrowed by a member"""
    # Find member instance and store in member
    member = find_item_by_id(library.members, member_id, "member_id")

    # If item type is book
    if item_type == "Book":
        # Find book instance in the members borrowed books and store in borrowed book
        borrowed_book = find_item_by_id(member.borrowed_books, item_id, "item_id")

        # If borrowed book is none
        if borrowed_book is None:
            # Print the book is not borrowed by the member and return false
            add_header(option)
            print(f"The Book with ID: {item_id}, is not borrowed by the member with ID: {member_id}")
            enter_continue()
            return False
        # Else return true
        return True

    # Else if item type is movie
    elif item_type == "Movie":
        # Find movie instance in the members borrowed movies and store in borrowed movie
        borrowed_movie = find_item_by_id(member.borrowed_movies, item_id, "item_id")

        # If borrowed movie is none
        if borrowed_movie is None:
            # Print the movie is not borrowed by the member and return false
            add_header(option)
            print(f"The Movie with ID: {item_id}, is not borrowed by the member with ID: {member_id}")
            enter_continue()
            return False
        # Else return true
        return True

# Define check item borrowed function
def check_item_borrowed(library, item_id, item_type):
    """Checks if an item is borrowed"""
    # If item type is book
    if item_type == "Book":
        # If is book borrowed function returns true
        if is_book_borrowed(library, item_id):
            # Print the book is borrowed and return true
            member = book_borrowed_by(library, item_id)
            print(f"!!! The book {item_id} is currently borrowed by member: {member.member_id} {member.name} !!!")
            print("Return the book before removing it")
            enter_continue()
            return True
        # Else return false
        return False
    
    # Else if item type is movie
    elif item_type == "Movie":
        # If is movie borrowed function returns true
        if is_movie_borrowed(library, item_id):
            # Print the movie is borrowed and return true
            member = movie_borrowed_by(library, item_id)
            print(f"!!! The movie {item_id} is currently borrowed by member: {member.member_id} {member.name} !!!")
            print("Return the movie before removing it")
            enter_continue()
            return True
        # Else return false
        return False
    
    # Else if item type is member
    elif item_type == "Member":
        # Find member instance and store in member
        member = find_item_by_id(library.members, item_id, "member_id")

        # If member has borrowed item
        if has_borrowed_item(member):
            # Print the member has borrowed item and return true
            print(f"!!! The member {item_id} {member.name} has a borrowed item !!!")
            print("Return the item before removing the member")
            enter_continue()
            return True
        # Else return false
        return False
  
# Define display main menu function     
def display_main_menu():
    """Displays the main menu"""

    # Print the user interface
    print("### LIBRARY MANAGEMENT SYSTEM ###")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. Add Member")
    print("5. Remove Member")
    print("6. Update Member")
    print("7. Issue Item")
    print("8. Return Item")
    print("9. Display Items")
    print("10. Display Members")
    print("0. Exit")

    # Return the users input
    return input("Please enter one of the options (0-10) here: ")

# Define choose item type function
def choose_item_type(option):
    """Makes the user choose the item type"""
    # Run loop until it is stopped
    while True:
        # Call add header function
        add_header(option)

        # Print different options
        print("1. Book")
        print("2. Movie")
        print("0. Back")

        # Set choice as the input of the user
        choice = input("Please enter one of the options (0-2) here: ")

        # Match choice to the cases and return item type as string
        match choice:
            case "1":
                return "Book"
            case "2":
                return "Movie"
            case "0":
                return "Back"
            case _:
                option = 0
                add_header(option)
                print("Please select a valid option")
                enter_continue()

# Define get valid digit function
def get_valid_digit(user_input, variable_control, option):
    """Gets a valid digit from the user"""
    # Run loop until it is stopped
    while True:
        # Call add header function
        add_header(option)

        # Check if user input is a digit and store in valid digit
        valid_digit = check_if_digit(user_input)

        # If valid digit is not false return valid digit
        if valid_digit is not False:
            return valid_digit
        
        # Call prompt wrong input function and store output as user input
        user_input = prompt_wrong_input(user_input, variable_control)

        # If user input is set to false return
        if user_input is False:
            return

# Define get valid input function
def get_valid_input(user_input, variable_control, option):
    """Gets a valid input from the user"""
    # Run loop until it is stopped
    while True:
        # Call add header function    
        add_header(option)

        # Check if user input is a nothing and store in valid input
        valid_input = check_if_nothing(user_input)
        
        # If valid input is false return user input
        if valid_input is False:
            return user_input
            
        # Call prompt empty input function and set output as user input
        user_input = prompt_empty_input(variable_control)

# Define get valid string function
def get_valid_string(user_input, variable_control, option):
    """Gets a valid string from the user"""
    # Run loop until it is stopped
    while True:
        # Call add header function
        add_header(option)

        # If variable control is update author or update director
        if variable_control == "Update Author" or variable_control == "Update Director":
            # Check if user input is nothing and store in valid input
            valid_input = check_if_nothing(user_input)
            
            # If valid input is true return user input
            if valid_input:
                return user_input
            
            # Check if user input is a string and store in valid input
            valid_input = check_if_string(user_input)

            # If valid input is not false return user input
            if valid_input is not False:
                return user_input
            
            # Call prompt wrong input function and store output as user input
            user_input = prompt_wrong_input(user_input, variable_control)
        
        # Else
        else:
            # Check if user input is nothing and store in invalid input
            invalid_input = check_if_nothing(user_input)

            # If invalid input is true
            if invalid_input:
                # Call prompt empty input and store output as user input and start loop over
                user_input = prompt_empty_input(variable_control)
                continue

            # Check if user input is a string and store output as valid string
            valid_string = check_if_string(user_input)
            
            # If valid string is not false return valid string
            if valid_string is not False:
                return valid_string
            
            # Call prompt empty input function and store output as user input
            user_input = prompt_wrong_input(user_input, variable_control)