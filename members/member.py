######################################################
#
#   
#
#
#
######################################################

# Create Member class
class Member():
    """Handles member instances"""
    # Define init method for Member class
    def __init__(self, member_id, name):
        # Define instance attributes for Member class
        self.__member_id = member_id
        self.name = name
        self._borrowed_books = []
        self._borrowed_movies = []

    # Define the instance method display info
    def display_info(self):
        """Displaying member information"""
        # Setup members borrowed items informations
        books_info = "\n".join(str(book) for book in self._borrowed_books) if self._borrowed_books else None
        movies_info = "\n".join(str(movie) for movie in self._borrowed_movies) if self.borrowed_movies else None
        # Set display none to 0
        display_none = 0

        # Print id and name of the member
        print(f"\nMember ID: {self.__member_id}, Name: {self.name}")

        # If books info is not none
        if not books_info is None:
            # Print the members borrowed books and subtract 1 from display none
            print(f"Borrowed Books: \n{books_info}")
            display_none = display_none - 1
        else:
            # Add 1 to display none
            display_none = display_none + 1
        
        # If movies info is not none
        if not movies_info is None:
            # Print the members borrowed movies and subtract 1 from display none
            print(f"Borrowed Movies: \n{movies_info}")
            display_none = display_none - 1
        else:
            # Add 1 to display none
            display_none = display_none + 1

        # If display none is greater than 0
        if display_none > 0:
            # Print no borrowed items
            print("No borrowed items")
        
        print("")

    # Define the instance method borrow item
    def borrow_item(self, item, item_type):
        """Appends an item to a member"""
        # If item type is book
        if item_type == "Book":
            # Append item to the list of borrowed books
            self._borrowed_books.append(item)
        # Else if item type is movie
        elif item_type == "Movie":
            # Append item to the list of borrowed movies
            self._borrowed_movies.append(item)

    # Define the instance method return item
    def return_item(self, item, item_type):
        """Removes an item from a member"""
        # If item type is book
        if item_type == "Book":
            # Remove item from the list of borrowed books
            self._borrowed_books.remove(item)
        # Else if item type is movie
        elif item_type == "Movie":
            # Remove item from the list of borrowed movies
            self._borrowed_movies.remove(item)
    
    # Create getter property for member id
    @property
    def member_id(self):
        return self.__member_id
    
    # Create setter for member id
    @member_id.setter
    def member_id(self, new_member_id):
            self.__member_id = new_member_id
    
    # Create getter property for borrowed books
    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    # Create getter property for borrowed movies
    @property
    def borrowed_movies(self):
        return self._borrowed_movies
    
