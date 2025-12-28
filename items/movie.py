######################################################
#
#   
#
#
#
######################################################

# Importing libraries
from .item import Item

# Create child class Movie of super class Item
class Movie(Item):
    """Handles movie instances"""
    # Define init method for Movie class
    def __init__(self, item_id, title, creator, copies):
        # Inheritate attributes from super class Item
        super().__init__(item_id, title, creator, copies)

    # Define the string method
    def __str__(self):
        """Returns the movie as a string"""
        return f"Movie ID: {self.item_id}, Title: {self.title}, Director: {self.creator}"
    
    # Define the instance method display info
    def display_info(self):
        """Displaying movie information"""
        print(f"\nMovie ID: {self.item_id}, Title: {self.title}, Director: {self.creator}, Available Copies: {self.copies}")
