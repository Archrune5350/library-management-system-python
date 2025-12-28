######################################################
#
#   
#
#
#
######################################################

# Importing libraries
from .item import Item

# Create child class Book of super class Item
class Book(Item):
    """Handles book instances"""
    # Define init method for Book class
    def __init__(self, item_id, title, creator, copies):
        # Inheritate attributes from super class Item
        super().__init__(item_id, title, creator, copies)

    # Define the string method
    def __str__(self):
        """Returns the book as a string"""
        return f"Book ID: {self.item_id}, Title: {self.title}, Author: {self.creator}"
    
    # Define the instance method display info
    def display_info(self):
        """Displaying book information"""
        print(f"\nBook ID: {self.item_id}, Title: {self.title}, Author: {self.creator}, Available Copies: {self.copies}")
