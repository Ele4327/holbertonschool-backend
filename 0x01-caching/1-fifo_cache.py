#!/usr/bin/python3

"""
Create a class that inherits and is
a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ BasicCache inherits from BaseCaching. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Must assign to the dictionary
            self.cache_data the item value for the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            dump = list(self.cache_data.keys())
            del self.cache_data[dump[0]]
            print("DISCARD: {}".format(dump[0]))

    def get(self, key):
        """
            Return the value linked to the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
