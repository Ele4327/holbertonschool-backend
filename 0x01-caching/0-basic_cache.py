#!/usr/bin/python3

"""
Create a class that inherits and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Assign to the dictionary the item
            value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
            Return the value linked to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
