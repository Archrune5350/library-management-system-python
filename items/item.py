######################################################
#
#   
#
#
#
######################################################

#Create super class Item
class Item():
    """Handles all item instances"""
    # Define init method for Item Class
    def __init__(self, item_id, title, creator, copies):
        # Define instance attributes for Item class
        self.__item_id = item_id
        self.title = title
        self.creator = creator
        self._copies = copies

    # Create getter property for item id
    @property
    def item_id(self):
        return self.__item_id
    
    # Create setter for item id
    @item_id.setter
    def item_id(self, new_item_id):
        self.__item_id = new_item_id

    # Create getter property for copies
    @property
    def copies(self):
        return self._copies
    
    # Create setter for copies
    @copies.setter
    def copies(self, new_copies):
        self._copies = new_copies
