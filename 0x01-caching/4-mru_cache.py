#!/usr/bin/env python3
"""
    Create a class MRUCache that inherits
    and is a caching system:
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching. """
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
            dump = list(self.cache_data.keys())
            del self.cache_data[dump[0]]
            print("DISCARD: {}".format(dump[0]))

    def get(self, key):
        """
            Must return the value in linked to key
        """
        item = self.cache_data.get(key)

        if item:
            del self.cache_data[key]
            self.cache_data[key] = item
        return item
