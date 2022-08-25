#!/usr/bin/env python3
"""
    Create a class that inherits and is
    a caching system:

"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ BasicCache inherits from BaseCaching. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Must assign to the dictionary
            the item value for the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """
            Must return the value linked to key.
        """
        item = self.cache_data.get(key)
        if key is None or key not in self.cache_data:
            return None
        if item:
            return self.cache_data[key]
