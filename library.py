######################################################
#
#   
#
#
#
######################################################

# Importing libraries
from ui import arrow

# Create Library class
class Library():
    """Handles all available actions for the library and stores items and members in lists"""
    # Define init method for Library class
    def __init__(self):
        # Define instance attributes for Library class
        self._books = []
        self._movies = []
        self._members = []

    # Define the instance method add item
    def add_item(self, new_item, item_type):
        """Adds a new item to the list of the item"""
        # Append new item to the list of books
        if item_type == "Book":
            self._books.append(new_item)
        # Append new item to the list of movies
        elif item_type == "Movie":
            self._movies.append(new_item)

    # Define the instance method remove item
    def remove_item(self, item, item_type):
        """Removes an item from the list of the item"""
        # Remove item from the list of books
        if item_type == "Book":
            self._books.remove(item)
        # Remove item from the list of movies
        if item_type == "Movie":
            self._movies.remove(item)

    # Define the instance method update item      
    def update_item(self, item, new_title, new_creator, new_copies):
        """Updates the information on a specific item in the list of the item"""
        # If new title is nothing
        if not new_title:
            # Set new title as old title
            new_title = item.title
        # If new creator is nothing
        if not new_creator:
            # Set new creator as old creator
            new_creator = item.creator
        # If new copies is nothing
        if not new_copies:
            # Set new copies as old copies
            new_copies = item.copies

        # Display current item information
        item.display_info()
        
        # Call arrow function
        arrow()

        # Set the current attributes as the new attributes
        item.title = new_title
        item.creator = new_creator
        item.copies = new_copies

        # Display new item information
        item.display_info()

    # Define the instance method add member
    def add_member(self, new_member):
        """Adds a member to the list of members"""
        # Append new member to the list of members
        self._members.append(new_member)

    # Define the instance method remove member
    def remove_member(self, member):
        """Removes a member from the list of members"""
        # Remove member from the list of members
        self._members.remove(member)

    # Define the instance method update member
    def update_member(self, member, new_name):
        """Updates the information on a specific member in the list of members"""
        # If new name is nothing
        if not new_name:
            # Set new name as old name
            new_name = member.name

        # Display current member information
        member.display_info()

        # Call arrow function
        arrow()

        # set the current attribute as the new attribute
        member.name = new_name

        # Display new member information
        member.display_info()
            
    # Define the instance method issue item
    def issue_item(self, item, item_type, member):
        """Issues an item to a member"""
        # Subtract 1 from copies of the item
        item.copies = item.copies - 1
        # Add item to the members borrowed item list
        member.borrow_item(item, item_type)

    # Define the instance method return item
    def return_item(self, item, item_type, member):
        """Returns an item from a member"""
        # Add 1 to copies of the item
        item.copies = item.copies + 1
        # Remove item from the members borrowed item list
        member.return_item(item, item_type)

    # Define the instance method display items
    def display_items(self, item):
        """Displays information of an item"""
        # Display item information
        item.display_info()

    # Define the instance method display members
    def display_members(self, member):
        """Displays information of a member"""
        # Display member information
        member.display_info()
    
    # Create getter property for list of books
    @property
    def books(self):
        return self._books
    
    # Create getter property for list of movies
    @property
    def movies(self):
        return self._movies
    
    # Create getter property for list of members
    @property
    def members(self):
        return self._members
    