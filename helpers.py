######################################################
#
#   
#
#
#
######################################################

# Define check if digit function
def check_if_digit(user_input):
    """Checks if the user input is only containing digits"""
    # Run loop until it is stopped
    while True:
        # Try to return user input as an integer
        try:
            return int(user_input)
        # If error happens return false
        except ValueError:
            return False
            
# Define check if string function
def check_if_string(user_input):
    """Checks if the user input is only containing letters"""
    # If instance is an integer
    if isinstance(user_input, int):
        # Set user input as a string
        user_input = str(user_input)

    # If any characters in the user input is a digit
    if any(char.isdigit() for char in user_input):
        # Return false
        return False
    # Else return user input
    return user_input

# Define check if nothing function
def check_if_nothing(user_input):
    """Checks if the user input is not containing anything"""   
    # If user input contains something
    if user_input:
        # Return false
        return False
    # Else return true
    return True

# Define find item by id function
def find_item_by_id(items, item_id, attr_name):
    """Finds an item in the list of items with the item id"""
    # For all items in the list of items
    for item in items:
        # If the item id is the same as the given id
        if getattr(item, attr_name) == item_id:
            # Return item
            return item
    # Else return none
    return None

# Define is item available function
def is_item_available(item):
    """Checks if an item is existing and available"""
    # Return the item if the item exist and copies of the item is greater than 0
    return item if item and item.copies > 0 else None

# Define is missing function
def is_missing(variable):
    """Checks if variable contains anything"""
    # If variable contains anything
    if variable:
        # Return false
        return False
    # Else return true
    return True

# Define is book borrowed function
def is_book_borrowed(library, book_id):
    """Checks if a book is borrowed"""
    # For all members in the list of members
    for member in library.members:
        # If any book id in the members borrowed books list is the same as the given book id
        if any(book.item_id == book_id for book in member.borrowed_books):
            # Return true
            return True
    # Else return false
    return False

# Define is movie borrowed function
def is_movie_borrowed(library, movie_id):
    """Checks if a movie is borrowed"""
    # For all members in the list of members
    for member in library.members:
        # If any movie id in the members borrowed movies list is the same as the given movie id
        if any(movie.item_id == movie_id for movie in member.borrowed_movies):
            # Return true
            return True
    # Else return false
    return False

# Define has borrowed item
def has_borrowed_item(member):
    """Checks if a member has a borrowed item"""
    # Return the length of the items lists if one list is greater than 0
    return len(member.borrowed_books) > 0 or len(member.borrowed_movies) > 0

# Define book borrowed by
def book_borrowed_by(library, book_id):
    """Returns the member that has borrowed the book"""
    # For all members in the list of members
    for member in library.members:
        # If any book id in the members borrowed books list is the same as the given book id
        if any(book.item_id == book_id for book in member.borrowed_books):
            # Return member
            return member

# Define movie borrowed by    
def movie_borrowed_by(library, movie_id):
    """Returns the member that has borrowed the movie"""
    # For all members in the list of members
    for member in library.members:
        # If any movie id in the members borrowed movies list is the same as the given movie id
        if any(movie.item_id == movie_id for movie in member.borrowed_movies):
            # Return member
            return member